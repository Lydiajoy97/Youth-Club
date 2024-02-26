from django.http import HttpResponse
from django.shortcuts import render
from .models import form
from django.contrib.auth.models import User


def home(request):
    return render(request, 'index.html')

def form_upload(request):

    if request.method=="POST":
       form = form._meta.get_fields()
       if form.is_valid(): 
            form.save()           
            return HttpResponse("Thanks for uploading your form! We will be in touch soon.") 

    else: 
        form = form_upload()

    return render(request,'form.html',{ 'form': form })

