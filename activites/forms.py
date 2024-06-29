from .models import ActivityForm
from django import forms

class HaveYourSayForm(forms.ModelForm):
    class Meta:
        model = ActivityForm
        exclude = 'status', 'approved', 'created_on'