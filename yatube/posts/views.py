from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts(request, slug=None):
    template = 'posts/group_list.html'
    return render(request, template)