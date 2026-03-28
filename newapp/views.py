from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,"home.html")

def news(request):
    return render(request,"news.html")

def acc(request):
    return render(request,"acc.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")
