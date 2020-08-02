from django.db import models
from datetime import datetime

# Post Models
class Post(models.Model):
	""" This models is for creating the Post on homepage. """
	post_title = models.CharField(max_length=200)
	post_content = models.TextField()
	post_published = models.DateTimeField('date published', default=datetime.now)

	def __str__(self):
		return self.post_title

#Feedback models
class Feedback(models.Model):
	""" This models is for get a feed from users"""
	#Rating field
	FEEDBACK_RATING = [
		('1', 'Excellent'),
		('2', 'Average'),
		('3', 'Good'),
		('4', 'Fair'),
		('5', 'Bad'),
	]

	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=150)
	rating = models.CharField(max_length=1, choices=FEEDBACK_RATING)
	message = models.TextField(default='N/A')
	
	def __str__(self):
		return self.name + " - " + self.get_rating_display()

# Contact Models
class Contact(models.Model):
	""" This models is for creating the Policies of school """
	poc = models.CharField(max_length=150)
	location  = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	web = models.CharField(max_length=100)
	updated_date = models.DateField(auto_now_add = False)

	def __str__(self):
		return "Updated on : " + str(self.updated_date)


class Advertisement(models.Model):
	""" This models is for creating the Advertisement """
	ad_name = models.CharField(max_length=150)
	ad_photo = models.ImageField(upload_to='ads/%Y/%m/%d/', blank=False)
	ad_updated_date = models.DateField(auto_now_add = True)
	ad_expire_date = models.DateField(auto_now_add = False)

	def __str__(self):
		return str(self.ad_name)