# from geeks for geeks
from django import forms

class UploadForm(forms.Form):

    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=254)
    age = forms.CharField(max_length=20)
    group_attending = forms.CharField(max_length=200)
    photo_consent = forms.BooleanField()
    addional_information = forms.CharField(max_length=700)
    consent_letter = forms.FileField()