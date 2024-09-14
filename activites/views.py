from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, TemplateView
from .models import ActivityForm
from .forms import HaveYourSayForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin 


# Class views from code.any youtube tutorials

class ActivityFormList(ListView):
    queryset = ActivityForm.objects.filter(status=1)
    template_name = "activityform_list.html"
    fields = ['game_ideas', 'author']
    paginate_by = 9

class RedirectView(TemplateView):
    template_name = "redirect2.html"

class HaveYourSay(LoginRequiredMixin, CreateView):
    form_class = HaveYourSayForm 
    template_name = "activites/addactivity.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = "redirect2.html/"


class UpdatePostView(LoginRequiredMixin, UpdateView): 
    model = ActivityForm
    template_name = 'activites/editactivity.html'
    fields = ['game_ideas']
    success_url = "redirect2.html"
    success_message = "Your suggestion has been edited!"
    def edit_posts(request, pk=None):
        obj = get_object_or_404(YourModel, pk=pk, user=request.user)
        return  render(request, 'activity.html',)
    

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = ActivityForm
    template_name = 'activites/deleteactivity.html'
    success_url = 'deleted.html'
    success_message = "Your form has been deleted successfully."
