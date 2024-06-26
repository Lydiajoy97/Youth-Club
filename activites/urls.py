from . import views
from django.urls import path


urlpatterns = [
    path('', views.ActivityFormList.as_view(), name= "activites"),
]