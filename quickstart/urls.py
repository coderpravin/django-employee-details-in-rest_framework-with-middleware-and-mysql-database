from django.urls import path
from .import views
urlpatterns = [
    path('', views.employeeListView, name ='employeeListView'),
    path('user', views.userListView, name ='userListView'),
]