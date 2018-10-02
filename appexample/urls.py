from django.urls import path
from . import views

urlpatterns = [
  path('', views.Index.as_view(), name='index'),
  path('user/new', views.UserEditView.as_view(), name='index'),
  path('user/edit/<int:pk>/', views.UserEditView.as_view(), name='index'),
]