from . import views
from django.urls import path


urlpatterns = [
    path('', views.ActivityFormList.as_view(), name='activityform'),
    path('<slug:slug>/', views.activites_detail, name="activityform_detail"),
]