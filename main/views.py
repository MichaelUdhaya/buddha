from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages

#Auth & user
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm

#utiltis
from datetime import datetime

from .choices import FEEDBACK_RATING
from .models import Post, Feedback, Contact, Advertisement, Playlist, Videos
from quiz.models import Course


# Home Page
def home_view(request):
	""" Home Page """

	#get the recent post
	recent_post_count = Post.objects.count()
	post = Post.objects.filter(pk=recent_post_count)

	#Get all advertisment only expire date greater than today date.
	ads = Advertisement.objects.filter(ad_expire_date__gt = datetime.now()).order_by('-ad_updated_date')

	#Get all post by desending order
	post_lists = Post.objects.order_by('-post_published')[:4]

	# messages.success(request, 'Welcome to Buddha')

	context = {
		'post' : post,
		'post_lists' : post_lists,
		'ads' : ads,
	}

	return render(request, 'main/index.html', context)

# Post Page
def post_view(request, pk):
	"""Annoncement page """
	post = get_object_or_404(Post, pk=pk)
	all_posts = Post.objects.order_by('-post_published')

	paginator = Paginator(all_posts, 5)
	page = request.GET.get('page')
	paged_posts = paginator.get_page(page)

	context = {
		'post' : post,
		'all_posts' : paged_posts,
	}

	return render(request, 'main/post.html', context)

# Post List
def post_list(request):
	"""Annoncements page """
	posts = Post.objects.order_by('-post_published')

	paginator = Paginator(posts, 10)
	page = request.GET.get('page')
	paged_posts = paginator.get_page(page)

	context = {
		'posts' : paged_posts,
	}

	return render(request, 'main/post_list.html', context)

# Facilities Page
def current_affairs_view(request):
	""" Facilities Page """
	posts = Post.objects.all()
	return render(request, 'main/current_affairs.html', {})

# Admissions Page
def courses_view(request):
	""" Courses Page """
	courses = Course.objects.all()
	return render(request, 'main/courses.html', {'courses':courses})

# Policies/Staffs Page
def policies_view(request):
	""" Policies/Staffs Page """
	#Get the last updated object's pk and pass to it
	# policy = Policy.objects.filter(pk=Policy.objects.count())
	return render(request, 'main/policies.html', {'policy':'policy'})

# Gallery Page
def gallery_view(request):
	""" Gallery Page """
	playlist = Playlist.objects.order_by('-id')

	context = {
		'playlist' : playlist,
	}

	return render(request, 'main/gallery.html', context)

# About Us Page
def about_us_view(request):
	""" About Us Page """
	posts = Post.objects.all()
	return render(request, 'main/about.html', {})

# Contact Us Page
def contact_us_view(request):
	""" About Us Page"""
	contact = Contact.objects.filter(pk=Contact.objects.count())
	return render(request, 'main/contact-us.html', {'contact':contact})

# Feedback Page
def feedback_view(request):
	""" Get the Feedback from users """
	if request.method == "POST":
		#Get forom values.
		name = request.POST['fullname']
		email = request.POST['email']
		rating = request.POST['rating']
		message = request.POST['feedback']

		feedback = Feedback(name=name, email=email, rating=rating, message=message)

		feedback.save()

		messages.success(request, ' Hi '+ name + '! Your feedback submitted successfully!')

		return redirect('main:url_home')
	else:
		return render(request, 'main/feedback.html', {'FEEDBACK_RATING': FEEDBACK_RATING})

#Authentication
def signup_view(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.profile.dob = form.cleaned_data.get('birth_date')
			user.profile.mobile = form.cleaned_data.get('mobile')
			user.profile.email = form.cleaned_data.get('email')
			user.profile.qulification = form.cleaned_data.get('qulification')
			user.profile.preparing_exam_from = form.cleaned_data.get('preparing_exam_from')
			username = form.cleaned_data.get('username')
			user = form.save()
			messages.success(request, f"New account created for {username}")
			login(request, user)
			return redirect('main:url_home')
		else:
			messages.error(request, f"Please correct the error below!")
			return render(request, 'main/sign-up.html', context = {'form':form})
	else:
		form = UserForm
		return render(request, 'main/sign-up.html', context = {'form':form})


def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			print("username : " + username)
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f'Welcome {username}!')
				return redirect('main:url_home')
			else:
				messages.error(request, "Username or Password is incorrect")
		else:
			messages.error(request, "Username or Password is incorrect")
	form = AuthenticationForm
	return render(request, 'main/login.html', {'form':form})

def logout_view(request):
	logout(request)
	messages.success(request, 'Logout successfully!')
	return redirect('main:url_login')