from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .forms import HaveYourSayForm
from .models import ActivityForm

class ActivityFormList(generic.ListView):
    model = ActivityForm

# def get_activity(request):
#     if request.method == "POST":
#         form = HaveYourSayForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect("activites/")

#     else:
#         form = ActivityForm()

#     return render(request, "activites.html", { "form": form })  