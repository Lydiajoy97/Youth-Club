from django.http import HttpResponse
from django.shortcuts import render
from .models import form
from django.contrib.auth.models import User


def home(request):
    return render(request, 'index.html')

def form(request):
    User._meta.get_fields()
    if request.method == "POST":
        if form.is_valid():
            file is saved
            form.save()
            return HttpResponse("Thanks for uploading your consent form! We will be in touch soon")
    else:
        return render(request, "index.html")

