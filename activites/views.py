from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import ActivityForm
from .forms import HaveYourSayForm
from django.http import HttpResponseRedirect

class ActivityFormList(ListView):
    queryset = ActivityForm.objects.filter(status=1)
    template_name = "activityform_list.html"
    paginate_by = 6

class ActivityDetailView(DetailView):
    model: ActivityForm
    template_name = 'activity_detail.html'

# From youtube 
class HaveYourSay(CreateView):
    form_class = HaveYourSayForm 
    template_name = "activites/addactivity.html"
    success_url = '/'
    success_message = "Your suggestion has been submitted and is awaiting approval."

def activity_detail(request, slug):

    queryset = ActivityForm.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    activity = post.activity.all().order_by("-created_on")
    activity_count = post.activitys.filter(approved=True).count()
    if request.method == "POST":
        activity_form = ActivityForm(data=request.POST)
        if activity_form.is_valid():
            activity = activity_form.save(commit=False)
            activity.name = request.user
            activity.post = post
            activity.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Suggestion submitted and awaiting approval'
            )

    activity_form = ActivityForm()


# def activity_edit(request, slug):
#     if request.method == "POST":
#         queryset = ActivityForm.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         activity = get_object_or_404(ActivityForm, pk=activity_id)
#         activity_form = ActivityForm(data=request.POST, instance=activity)

#         if activity_form.is_valid() and activity.name == request.user:
#             activity = activity_form.save(commit=False)
#             activity.post = post
#             activity.approved = False
#             activity.save()
#             messages.add_message(request, messages.SUCCESS, 'Your suggestion has been Updated!')
#         else:
#             messages.add_message(request, messages.ERROR, 'Error updating your suggestion!')

#     return HttpResponseRedirect(reverse('addactivity', args=[slug]))

class UpdatePostView(UpdateView):
    model = ActivityForm
    template_name = 'activites/editactivity.html'
    fields = ['game_ideas', 'first_name',]
    success_url = '/'