from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import ChildrensForm
from .models import UploadForm

# Help to write code From https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page and walkthrough.
# https://docs.djangoproject.com/en/5.0/intro/tutorial03/ 
def home(request):
    return render(request, './index.html')

# from geeks for geeks and https://www.youtube.com/watch?v=EX6Tt-ZW0so
def upload_view(request):

    form = ChildrensForm()
    if request.method == "POST":
       form = ChildrensForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect ('/form/post/redirect.html')

    context = {'form' : form}
    return render(request, "form.html", context)

class RedirectView(TemplateView):
    template_name = "redirect.html"