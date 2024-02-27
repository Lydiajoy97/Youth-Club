from django.http import HttpResponse
from django.shortcuts import render
from .models import form
from django.contrib.auth.models import User


def home(request):
    return render(request, 'index.html')

def form_upload(request):
# help from https://stackoverflow.com/questions/3106295/django-get-list-of-model-fields
# help from https://docs.djangoproject.com/en/5.0/ref/models/meta/
    if request.method=="POST":
       form = form._meta.get_fields()
       if form.is_valid(): 
            form.save()           
            return HttpResponse("Thanks for uploading your form! We will be in touch soon.") 

    else: 
        form = form_upload()

    return render(request,'form.html',{ 'form': form })

