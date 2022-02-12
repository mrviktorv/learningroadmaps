from django.urls import path
from .views import TopicDetailView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('for-teachers/', views.for_teachers, name='for-teachers'),
    path('support/', views.support, name='support'),
    path('help/', views.help, name='help'),
    path('contacts/', views.contacts, name='contacts'),
    path('sample/', views.sample, name='sample'),
    path('pytest/', views.pytest, name='pytest'),
    path('glossary/', views.glossary, name='glossary'),
    path('feedback/', views.feedback, name='feedback'),
    
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic-detail'),
    
]