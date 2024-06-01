from django.http import HttpResponse
from django.contrib import admin
from django.shortcuts import render  #this is bcz we have to render html pages

#############returning text###################333
# def homepage(request):
#     return HttpResponse("this is homepage")

# def about(request):  #the request part contains all the information about the request that was made
#     return HttpResponse("About page")

####################returning templates#################33
def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

