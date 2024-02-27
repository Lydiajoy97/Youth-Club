from django.http import HttpResponse
from django.shortcuts import render
from .models import form
from django.contrib.auth.models import User
from django.views.generic.list import ListView

def home(request):
    return render(request, 'index.html')

class formlist(ListView):
# help from https://stackoverflow.com/questions/3106295/django-get-list-of-model-fields
# help from https://docs.djangoproject.com/en/5.0/ref/models/meta/
    model = form
    fields = ['all']

def form(request):
    return render(request, 'form.html')

