from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import ActivityForm
from .forms import HaveYourSayForm

class ActivityFormList(generic.ListView):
    queryset = ActivityForm.objects.filter(status=1)
    template_name = "activityform_list.html"
    paginate_by = 6

# From youtube 
class HaveYourSay(generic.CreateView):
    form_class = HaveYourSayForm 
    template_name = "addactivity.html"
    success_url = '/'
    success_message = "Your suggestion has been submitted and is awaiting approval."