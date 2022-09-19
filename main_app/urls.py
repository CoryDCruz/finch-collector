from django.urls import path
from . import views

urlpatterns =[
  path('', views.home),
  path('about/', views.about),
  path('finches/', views.finches_index),
  path('finches/<int:finch_id>/', views.finch_details, name='details'),
]
