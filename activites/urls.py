from . import views
from django.urls import path
from .views import UpdatePostView, DeletePostView, TemplateView

# URL Paths built using code.any youtube tutorials

urlpatterns = [
    path('', views.ActivityFormList.as_view(), name='activityform'),
    path('addactivity/', views.HaveYourSay.as_view(), name='addactivity'),
    path('addactivity/redirect2.html/', TemplateView.as_view(template_name='redirect.html')),
    path('edit/redirect2.html/', TemplateView.as_view(template_name='redirect.html')),
    path('edit/<int:pk>', UpdatePostView.as_view(), name='editactivity'),
    path('activites/<int:pk>/delete', DeletePostView.as_view(), name='deleteactivity'),
    path('activites/<int:pk>/deleted.html', TemplateView.as_view(template_name='activites/deleted.html')),
]