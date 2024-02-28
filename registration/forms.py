# from geeks for geeks
from django import forms
from django.forms import ModelForm
from .models import UploadForm 

class ChildrensForm(ModelForm):
    class Meta:
        model = UploadForm
        fields = '__all__'