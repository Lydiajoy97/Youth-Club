from . import views
from django.urls import path
from .views import TemplateView

urlpatterns = [
        path('', views.home, name='home'),
        path('form/post', views.upload_view, name='form'),
        path('form/post/redirect.html', TemplateView.as_view(template_name='redirect.html')),
]