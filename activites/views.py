from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import ActivityForm


class ActivityFormList(generic.ListView):
    model = ActivityForm
    queryset = ActivityForm.objects.filter(status=1)
    template_name = "activites.html"
    paginate_by = 6


class ActivityFormDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = ActivityForm.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "activites.html",
            {
                "post": post,
            } 
        )