# from geeks for geeks
from django import forms
from .models import UploadForm

class UploadForm(forms.ModelForm):

    class Meta: 
        model = UploadForm 
        fields = "__all__"