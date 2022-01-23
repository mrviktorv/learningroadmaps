from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'englishmap/home.html', {'title': 'Home'})
  
def for_teachers(request):
    return render(request, 'englishmap/for-teachers.html', {'title': 'For teachers'})

def support(request):
    return render(request, 'englishmap/support.html', {'title': 'Support us'})

def help(request):
    return render(request, 'englishmap/help.html', {'title': 'Help'})

def contacts(request):
    return render(request, 'englishmap/contacts.html', {'title': 'Contacts'})    

def sample(request):
    return render(request, 'englishmap/sample.html', {'title': 'Sample'})   
