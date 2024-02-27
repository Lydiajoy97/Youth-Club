from . import views
from django.urls import path
from .views import formlist

urlpatterns = [
        path('', views.home, name='home'),
        path('form/', views.form, name='form'),
]