from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserForm(UserCreationForm):
	first_name = forms.CharField(max_length=100, help_text='You must enter your First Name', required=True)
	last_name = forms.CharField(max_length=100, required=False)
	birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
	mobile = forms.CharField(max_length=15, help_text="Enter your primary mobile number(max length = 15)", required=True)
	email = forms.EmailField(required=True, help_text='You must enter Email')
	street = forms.CharField(max_length=250, required=False)
	city = forms.CharField(max_length=50, required=False)
	qulification = forms.CharField(max_length=60, help_text="Enter your qulification here!")
	preparing_exam_from = forms.DateField(required=True, help_text='Required. Format: YYYY-MM-DD')

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "birth_date", "mobile", "email", "street", "city", "qulification", "preparing_exam_from", "password1", "password2")