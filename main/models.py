from django.db import models

#Default User models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#choice
from main import choices

#utility
from datetime import datetime

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(default='1900-01-01')
    gender = models.PositiveSmallIntegerField(choices=choices.GENDER, null=False, blank=False, default=3)
    mobile = models.CharField(max_length=15, blank=False)
    street = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=50, default='Chennai', blank=True)
    state = models.CharField(max_length = 150, choices = choices.INDIAN_STATES, default = 'TN') 
    qulification = models.CharField(max_length=60, blank=True)
    preparing_exam_from = models.DateField(default=datetime.now)
    photo = models.ImageField(upload_to='users/%Y%m%d/', blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


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
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=150)
	rating = models.CharField(max_length=1, choices=choices.FEEDBACK_RATING)
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