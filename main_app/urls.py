from django.urls import path
from . import views

urlpatterns =[
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/', views.finches_index, name='index'),
  path('finches/<int:finch_id>/', views.finch_details, name='details'),
  path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
  path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
  path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
  path('toys/', views.ToyList.as_view(), name='toys'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy_create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy_detail'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy_delete'),
  path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('finches/<int:finch_id>/assoc_toy/<int:toy_id>', views.assoc_toy, name='assoc_toy'),
  path('accounts/signup', views.signup, name='signup'),
  path('finches/<int:finch_id>/add_photo', views.add_photo, name='add_photo'),
]
