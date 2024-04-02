# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'info_manage'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job_list/<int:category_id>/', views.job_list, name='job_list'),
    path('add_collect/', views.add_collect, name='add_collect'),
    path('add_order/', views.add_order, name='add_order'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('input_score/', views.input_score, name='input_score'),
    path('my_collect/', views.my_collect, name='my_collect'),
    path('delete_collect/', views.delete_collect, name='delete_collect'),
    path('my_order/', views.my_order, name='my_order'),
    path('my_info/', views.my_info, name='my_info'),
    path('view_count/', views.view_count, name='view_count'),
    path('job_recommend/<int:user_id>/', views.user_based_recommendation, name='job_recommend'),
]
