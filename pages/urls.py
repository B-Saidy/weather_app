from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('news/<int:id>/', views.detail_news, name='detail_news'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>/', views.detail_project, name='detail_project'),
    path('contacts/', views.contacts, name='contacts'),

]

