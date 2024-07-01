from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import ActivityForm
from .forms import HaveYourSayForm
from django.http import HttpResponseRedirect

class ActivityFormList(generic.ListView):
    queryset = ActivityForm.objects.filter(status=1)
    template_name = "activityform_list.html"
    paginate_by = 6

# From youtube 
class HaveYourSay(generic.CreateView):
    form_class = HaveYourSayForm 
    template_name = "activites/addactivity.html"
    success_url = '/'
    success_message = "Your suggestion has been submitted and is awaiting approval."

def suggestion_edit(request, slug):
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        suggestion = get_object_or_404(ActivityForm, pk=activity_id)
        activity_form = ActivityForm(data=request.POST, instance=comment)

        if activity_form.is_valid() and suggestion.author == request.user:
            suggestion = activity_form.save(commit=False)
            suggestion.post = post
            suggestion.approved = False
            suggestion.save()
            messages.add_message(request, messages.SUCCESS, 'Your suggestion has been Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating your suggestion!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))