from . import views
from django.urls import path
from .views import UpdatePostView, DeletePostView

urlpatterns = [
    path('', views.ActivityFormList.as_view(), name='activityform'),
    path('addactivity/', views.HaveYourSay.as_view(), name='addactivity'),
    path('edit/<int:pk>', UpdatePostView.as_view(), name='editactivity'),
    path('activites/<int:pk>/delete', DeletePostView.as_view(), name='deleteactivity'),
]