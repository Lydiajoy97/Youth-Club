from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import ActivityForm

class ActivityFormList(generic.ListView):
    queryset = ActivityForm.objects.filter(status=1)
    template_name = "activityform_list.html"
    paginate_by = 6

def activites_detail(request, slug):
    queryset = ActivityForm.objects.filter(status=1)
    activity = get_object_or_404(queryset, slug=slug)
    return render(request, "activityform_list.html", {"activity": activity},)