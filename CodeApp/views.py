from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def quote_list(request):
    quoteList=quotes.objects.all()
    d={'quoteList':quoteList}
    return render(request,'quotes.html',d)


