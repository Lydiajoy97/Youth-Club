from . import views
from django.urls import path

urlpatterns = [
        path('', views.home, name='home'),
        path('form/post', views.upload_view, name='form'),
]