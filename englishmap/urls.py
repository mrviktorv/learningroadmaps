from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('for-teachers/', views.for_teachers, name='for-teachers'),
    path('support/', views.support, name='support'),
    path('help/', views.help, name='help'),
    path('contacts/', views.contacts, name='contacts'),
    path('sample/', views.sample, name='sample'),
]