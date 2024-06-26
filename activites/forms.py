from django import forms
from django.forms import ModelForm
from .models import ActivityForm

class HaveYourSayForm(ModelForm):
    class Meta:
        model = ActivityForm
        fields = '__all__'