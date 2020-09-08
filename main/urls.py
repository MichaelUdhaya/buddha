from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.home_view, name='url_home'),
    path('post/<int:pk>/', views.post_view, name='url_post'),
    path('all-posts-list/', views.post_list, name='url_post_list'),
    path('current-affairs/', views.current_affairs_view, name='url_current_affairs'),
    path('courses/', views.courses_view, name='url_courses'),
    path('policies-staffs/', views.policies_view, name='url_policies'),
    path('gallery/', views.gallery_view, name='url_gallery'),
    path('about-us/', views.about_us_view, name='url_about_us'),
    path('contact-us/', views.contact_us_view, name='url_contact_us'),
    path('feedback/', views.feedback_view, name='url_feedback'),
    #Auth
    path('signup/', views.signup_view, name='url_signup'),
    path('login/', views.login_view, name='url_login'),
    path('logout/', views.logout_view, name='url_logout'),
]
