from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .forms import HaveYourSayForm
from .models import ActivityForm

class ActivityFormList(generic.ListView):
    model = ActivityForm

def get_activity(request):

    form = HaveYourSayForm()
    if request.method == "POST":
       form = ActivityForm(request.POST)
       if form.is_valid():
        form.save()
        return redirect ('/')
        
    context = {'form' : form}
    return render(request, "activityform_list.html", context)