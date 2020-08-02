from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.home_view, name='url_home'),
    path('annoncement/<int:pk>/', views.post_view, name='url_post'),
    path('annoncements/', views.post_list, name='url_post_list'),
    path('facilities/', views.facilities_view, name='url_facilities'),
    path('admissions/', views.admissions_view, name='url_admissions'),
    path('policies-staffs/', views.policies_view, name='url_policies'),
    path('gallery/', views.gallery_view, name='url_gallery'),
    path('about-us/', views.about_us_view, name='url_about_us'),
    path('contact-us/', views.contact_us_view, name='url_contact_us'),
    path('feedback/', views.feedback_view, name='url_feedback'),
]
