from django.urls import path
from . import views

app_name = 'quiz'  # here for namespacing of urls.

urlpatterns = [
	path('', views.quiz_view, name='url_quiz'),
	path('<int:pk>/', views.take_quiz_view, name='url_take_quiz'),
	path('<int:pk>/quiz-live/', views.quiz_live_view, name='url_quiz_live'),
	path('<int:pk>/quiz-result/', views.quiz_result_view, name='url_quiz_result'),
	path('dashboard/', views.dashboard_view, name='url_dashboard'),
]