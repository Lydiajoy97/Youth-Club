from django.contrib import admin
from .models import UploadForm

# Register your models here.
# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
@admin.register(UploadForm)
class UploadFormAdmin(admin.ModelAdmin):
    pass 