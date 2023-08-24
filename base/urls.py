from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cordinator/', views.cordinator, name="cordinator"),
    path('description/<str:pk>/', views.description, name="description"),
    path('cordinator/manageTasks', views.manageTasks, name="manageTasks"),
    path('addTask', views.addTask, name='addTask'),
    path('updateTask/<str:pk>/', views.updateTask, name='updateTask'),
    path('deleteTask/<str:pk>/', views.deleteTask, name='deleteTask'),

    path('test/', views.test, name='test'),
]
