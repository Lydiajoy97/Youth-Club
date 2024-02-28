from django.shortcuts import render
from .models import About

# Help to write code From https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page and walkthrough.
# https://docs.djangoproject.com/en/5.0/intro/tutorial03/ 
# Create your views here.
def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about.html",
        {"about": about},
    )