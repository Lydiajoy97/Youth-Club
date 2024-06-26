from django.shortcuts import render
from django.views import generic
from .models import ActivityForm

class ActivityFormList(generic.ListView):
    queryset = ActivityForm.objects.all()
    template_name = "activites.html"