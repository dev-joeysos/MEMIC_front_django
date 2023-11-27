<<<<<<< HEAD
=======
"""
>>>>>>> a7ba93c (Update each page URL(#1))
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('401/', views.four_one, name='401'),
    path('404/', views.four_four, name='404'),
    path('faqs/', views.faqs, name='faqs'),
<<<<<<< HEAD
    path('feedback/', views.feedback, name='feedback'),
    path('input/', views.input, name='input'),
    path('record/', views.record, name='record'),
    path('style-guide/', views.style_guide, name='style-guide'),


]
=======
    path('record/', views.record, name='record'),
    path('style-guide/', views.style_guide, name='style-guide'),

    path('feedback/', views.feedback, name='feedback'),
    path('input/', views.input, name='input'),
]
"""

>>>>>>> a7ba93c (Update each page URL(#1))
