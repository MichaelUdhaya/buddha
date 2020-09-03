from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib import admin

#admin model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Post, Feedback, Contact, Advertisement, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
	inlines = (ProfileInline, )
	list_display = ('username', 'email', 'first_name', 'last_name', 'dob', 'gender', 'mobile', 'is_staff')
	list_select_related = ('profile', )

	def dob(self, instance):
		"""
		Append it to the list_display, because the dob field is defined in a external model.
		So for the Django Admin understand how to display the location attribute, we have to play it this way.
		"""
		return instance.profile.dob

	def gender(self, instance):
		return instance.profile.get_gender_display()

	def mobile(self, instance):
		return instance.profile.mobile

	#is just to display it prettier in the table header
	dob.short_description = 'Date of Birth'
	gender.short_description = 'Gender'
	mobile.short_description = 'Mobile Number'



	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class PostAdmin(admin.ModelAdmin):
	fieldsets =  [
		('Title/date', {'fields' : ['post_title','post_published']}),
		('Content', {'fields' : ['post_content']}),
		]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()},
		}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(Advertisement)


#User models override
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)