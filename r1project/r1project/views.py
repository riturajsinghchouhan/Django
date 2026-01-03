from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, Welcome to about page wrold")

def contact(request):
    return HttpResponse("Hello , Welcome to contact page")