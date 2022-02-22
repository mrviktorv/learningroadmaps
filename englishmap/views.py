from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Topic, Comment, Reply, LayoutRow, LayoutRow1
from django.views.generic import ListView, DetailView, CreateView
from .forms import CommentForm, ReplyForm
from django.core.paginator import Paginator
from django.urls import reverse

def home(request):
    layout = LayoutRow.objects.all().order_by('id')
    layout1 = LayoutRow1.objects.all().order_by('id')

    context = {
        'topics': Topic.objects.all(),
        'rows': layout,
        'rows1': layout1,
        'title': 'Home'
    }
    return render(request, 'englishmap/home.html', context)
  
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




class topics: 
    def __init__(self, id, name, short, full, links): 
        self.id = id 
        self.name = name
        self.short = short
        self.full = full
        self.links = links
        self.letter = name[0].lower()



class rows: 
    def __init__(self, arrL, arrC, arrR, topL, topC, topR): 
        self.arrL = arrL
        self.arrC = arrC
        self.arrR = arrR
        self.topL = topL
        self.topC = topC
        self.topR = topR
   
     
# toplist = [
#     topics(
#         1, 
#         'Noun',
#         'Dog, apple, cat, house + I, you, he, she, it, we, they',
#         "A noun is a word that refers to a thing (book), a person (Betty Crocker), an animal (cat), a place (Omaha), a quality (softness), an idea (justice), or an action (yodeling). It's usually a single word, but not always: cake, shoes, school bus, and time and a half are all nouns.",
#         'man.com'
#     ), 
#     topics(
#         2, 
#         'Verb',
#         'go, eat, dance + be, is, are',
#         'Verbs are words that show an action (sing), occurrence (develop), or state of being (exist). Almost every sentence requires a verb. The basic form of a verb is known as its infinitive. The forms call, love, break, and go are all infinitives. Almost all verbs have two other important forms called participles.',
#         'manny.com'
#     )
# ] 

# layout = [
#     rows(
#     'arrowL',
#     'arrowC', 
#     'arrowC', 
#     2,
#     1,
#     1,
#     ),
#     rows(
#     'arrowL',
#     'arrowR', 
#     '', 
#     3,
#     2,
#     0,
#     )
# ]

alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
"U", "V", "W", "X", "Y", "Z"]




def glossary(request):
    context = {
        'alph': alph,
        'topics': Topic.objects.all().order_by('title'),
        'title': 'Glossary'
    }
    return render(request, 'englishmap/glossary.html', context)

def feedback(request):
    form = CommentForm(request.POST or None)
    formR = ReplyForm(request.POST or None)

    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
            if form.is_valid():
                form.save()
                form = CommentForm()
        elif request.POST.get("form_type") == 'formTwo':
            if formR.is_valid():
     
                formR.instance.comment_id = int(request.POST.get("comment_id"))
   
                formR.save()
                formR = ReplyForm()
           
                return HttpResponseRedirect(reverse("feedback"))
            else:
                raise TypeError("Reply has not been submitted!")
        else:
            raise TypeError("Reply has not been submitted!")
        
    comment_list = Comment.objects.all().order_by('-timestamp')
    paginator = Paginator(comment_list, 10) # Show N per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'comments': Comment.objects.all().order_by('-timestamp'),
        'page_obj': page_obj,
        'form': form,
        'formR': formR,
        'title': 'Feedback'
    }
    return render(request, 'englishmap/feedback.html', context)
    



class TopicDetailView(DetailView):
    model = Topic
