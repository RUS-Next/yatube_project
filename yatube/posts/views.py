from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = 'posts/index.html'
    context = {
        'text'  :  "Это главная страница проекта Yatube"
    }
    return render(request, template,  context)

def group_posts(request, slug=None):
    template = 'posts/group_list.html'
    context = {
        'text': "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, template,  context)