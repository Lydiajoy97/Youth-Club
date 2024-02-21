from . import views
from django.urls import path

urlpatterns = [
        path('', views.upload_form.as_view(), name='home'),
]