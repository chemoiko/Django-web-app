from django.shortcuts import render
from .models import Article


# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')       #they aare ordered by date here i.e the latest the first
    return render(request,'articles/article_list.html', {'articles':articles})      #we have created a dictionary that we are going to send to the template