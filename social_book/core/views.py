from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request) -> HttpResponse:
    return HttpResponse('<h1>Welcome to Social Book</h1>')
    
    