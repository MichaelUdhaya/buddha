from django.contrib import admin
from django.db import models

#Widgets
from tinymce.widgets import TinyMCE
from .models import Course, Question, UserDashboard

class CourseAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()},
		}

class QuestionAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()},
		}

admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserDashboard)