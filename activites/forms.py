from django import forms

class HaveYourSayForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=254)
    game_ideas = forms.CharField(max_length=700)
