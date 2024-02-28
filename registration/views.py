from django.http import HttpResponse
from django.shortcuts import render
from .models import form
from django.contrib.auth.models import User

# Help to write code From https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page and walkthrough.
# https://docs.djangoproject.com/en/5.0/intro/tutorial03/ 
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

