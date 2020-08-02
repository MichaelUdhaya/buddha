from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib import admin
from .models import Post, Feedback, Contact, Advertisement


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