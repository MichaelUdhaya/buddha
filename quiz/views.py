from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Count, Min, Sum, Max
from django.core.paginator import Paginator
from django.contrib import messages

from django.contrib.auth.decorators import login_required

#utilites
from datetime import datetime

from .models import Course, Question, UserDashboard


def quiz_view(request):
	try:
		all_course = Course.objects.order_by('exam_number')
		paginator = Paginator(all_course, 5)
		page = request.GET.get('page')
		paged_courses = paginator.get_page(page)
		all_course = paged_courses
	except:
		course = None

	context = {
		'all_course' : all_course,
	}
	return render(request, 'quiz/home.html', context)

@login_required(login_url='/login/')
def take_quiz_view(request, pk):
	"""Take Quiz """
	course = get_object_or_404(Course, pk=pk)

	context = {
		'course' : course,
	}

	return render(request, 'quiz/take_quiz.html', context)

def quiz_live_view(request, pk):

	course= get_object_or_404(Course, pk=pk)
	course_name = course.syallbus
	print(course_name)

	""" from the Qustion model we filter, only matching pk to Course"""
	questions = Question.objects.filter(course__syallbus=course_name)

	context = {
		'questions' : questions,
		'course' : course,
	}
	return render(request, 'quiz/quiz_live.html', context)


def quiz_result_view(request, pk):
	""" 
		Get answer via Request. then calculate and store it in Dictionary Values
		Dictionary valus: 1. Question  - 2. Answer - 3. User_Answer - 4. Status - 5. Marks
		general values : 1. total_marks - 2. marks - 3. percentage - 4. result - 5. quiz_name
	"""

	course = get_object_or_404(Course, pk=pk)
	course_name = course.syallbus
	print(course_name)

	#get question model by primary key
	questions = Question.objects.filter(course__syallbus=course_name)

	#get sum of mark value from Quetion model
	total_marks = Question.objects.filter(course__syallbus=course_name).aggregate(Sum('mark_value'))
	total_marks = total_marks['mark_value__sum'] #get only value from dictionary

	answers = []
	intCount = 1
	marks = 0

	for q in questions:
		dicData = {} #Init new dictionary for every iteration

		dicData.update({'Question': q.question}) # Add key and value to empty dictionary
		dicData.update({'Answer': q.answer})

		# create new variable for question number. webpage return value in 'opt1:<answer>'
		qus_number = 'opt' + str(intCount) 

		# Try to get anser by it's qus number like 'opt1'. It will return the value of 'opt1 key'.
		try:
			user_answer = request.GET[qus_number]
		# if answer was not found then we assign NA value to answer
		except:
			user_answer = 'NA'

		dicData.update({'User_Answer': user_answer})

		#if user answer was matched with orginal answer(from model) then we increse the mark value
		if user_answer == q.answer:
			dicData.update({'Status': True })
			dicData.update({'Marks': int(q.mark_value) })
			marks += q.mark_value #increase the mark value(from model field)
		else:
			dicData.update({'Status': False })
			dicData.update({'Marks': 0 })

		answers.append(dicData) #add dictionary to list
		intCount += 1

	#Get Percentage
	percentage = float((int(marks) / int(total_marks)) * 100)

	#Calculate Result
	if float(percentage) > 40:
		print("Pass")
		result = "Pass"
	else:
		print("Fail")
		result = "Fail"

	print("user : " + str(request.user))

	#if list conatains any data, then update to dashboard
	if len(answers) > 0:
		# quiz_name = questions.course
		dashboard_update = UserDashboard(user=request.user,
										quiz_name=course_name,
										# quiz_date=datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
										quiz_score=f'{marks} out of {total_marks}',
										quiz_timing="20 mins",
										quiz_result=result,
										)
		dashboard_update.save()
		print("Dashboard updated successfully!")

	context = {
		'results' : answers,
		'total_marks' : total_marks,
		'marks': marks,
		'percentage' : percentage,
		'result_status': result,
	}
	return render(request, 'quiz/quiz_result.html', context)

def dashboard_view(request):
	
	try:
		my_dashboard = UserDashboard.objects.filter(user=request.user).order_by('-quiz_date')
		paginator = Paginator(my_dashboard, 10)
		page = request.GET.get('page')
		paged_courses = paginator.get_page(page)
		dashboard = paged_courses

		total_count = UserDashboard.objects.filter(user=request.user).aggregate(Count('quiz_name'))['quiz_name__count']
		pass_count = UserDashboard.objects.filter(user=request.user, quiz_result="Pass").aggregate(Count('quiz_name'))['quiz_name__count']
		fail_count = UserDashboard.objects.filter(user=request.user, quiz_result="Fail").aggregate(Count('quiz_name'))['quiz_name__count']
		max_count = UserDashboard.objects.filter(user=request.user).aggregate(Max('quiz_score'))['quiz_score__max']
	except:
		dashboard = None
		total_count = 0
		pass_count = 0
		fail_count = 0
		max_count = 0

	context = {
		'dashboard' : dashboard,
		'total_count' : total_count,
		'pass_count' : pass_count,
		'fail_count' : fail_count,
		'max_count' : max_count,
	}
	return render(request, 'quiz/dashboard.html', context)