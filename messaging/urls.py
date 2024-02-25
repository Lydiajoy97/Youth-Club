from . import views
from django.urls import path

urlpatterns = [
    path('', views.Contactform, name='contact'),
]