
from django.urls import path
from . import views

urlpatterns = [
    path('', views.osama_view, name='osama'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dash/', views.dashBoard, name='dash'),
    path('course_search/', views.course_search, name='course_search'),
    path('register_courses/', views.reg_cs, name='register_courses'),
    path('mycourse/',views.Mycourses,name='mycs'),
]
