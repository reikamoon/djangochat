from django.shortcuts import render
from django.views import generic
from django.template.loader import get_template

# Create your views here.
def IndexView(request):
    get_template('index.html')
