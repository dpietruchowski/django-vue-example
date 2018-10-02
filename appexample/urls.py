from django.urls import path
from . import views

urlpatterns = [
  path('', views.IndexView.as_view()),
  path('user/new', views.UserEditView.as_view()),
  path('user/edit/<int:pk>/', views.UserEditView.as_view()),
  path('users', views.UserListView.as_view()),

  # REST Api
  path('user/list', views.UserSearchView.as_view()),
]