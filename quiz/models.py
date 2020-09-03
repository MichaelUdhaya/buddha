from django.db import models
from django.contrib.auth.models import User

#Utilities
from datetime import datetime


class Course(models.Model):
	exam_number = models.IntegerField()
	exam_date = models.DateField(default=datetime.now)
	syallbus = models.TextField(default='N/A')

	def __str__(self):
		return str(self.exam_number) + ' - ' + str(self.exam_date)

class Question(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	question = models.TextField(blank=False)
	option1 = models.CharField(max_length=100, blank=False)
	option2 = models.CharField(max_length=100, blank=False)
	option3 = models.CharField(max_length=100, blank=False)
	option4 = models.CharField(max_length=100, blank=False)
	answer = models.CharField(max_length=100, blank=False)
	total_time = models.IntegerField(default=2, blank=False, help_text="Duration for this question. Enter in Minutes")
	mark_value = models.IntegerField(default=0, help_text="Enter mark value", blank=False)

	def __str__(self):
		return str(self.question[30:])

class UserDashboard(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	quiz_name = models.TextField(blank=False)
	quiz_date = models.DateTimeField(default=datetime.now)
	quiz_score = models.CharField(max_length=100, blank=False)
	quiz_timing = models.CharField(max_length=100, blank=False)
	quiz_result = models.CharField(max_length=10, blank=False)

	def __str__(self):
		return str(self.quiz_name[30:]) + " - " + str(self.quiz_date)