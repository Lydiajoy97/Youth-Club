from . import views
from django.urls import path

urlpatterns = [
    path('', views.ActivityFormList.as_view(), name='activityform'),
    path('addactivity/', views.HaveYourSay.as_view(), name='addactivity'),
     path('<slug:slug>/edit_activity/<int:activity_id>',
        views.activity_edit, name='edit_activity'),
]