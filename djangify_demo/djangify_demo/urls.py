from django.contrib import admin
from django.urls import path

import demo.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', demo.views.index, name='index'),
    path('401/', demo.views.four_one, name='401'),
    path('404/', demo.views.four_four, name='401'),
    path('feedback/', demo.views.feedback, name='feedback'),
    path('input/', demo.views.input, name='input'),
    path('record/', demo.views.record, name='record'),
    path('style-guide/', demo.views.style_guide, name='style-guide'),
    path('faqs/', demo.views.faqs, name='faqs'),

]
