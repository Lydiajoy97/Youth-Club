from django.http import HttpResponse
from django.shortcuts import render
from .models import form
from django.contrib.auth.models import User

def home(request):
    return render(request, 'index.html')

def formlist(request):
    """
    Renders the form page
    """
    Form = form.objects.all()

    return render(
        request,
        "form.html",
        {"form": form},
    )

