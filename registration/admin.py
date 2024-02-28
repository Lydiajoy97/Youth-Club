from django.contrib import admin
from .models import UploadForm

# Register your models here.
@admin.register(UploadForm)
class UploadFormAdmin(admin.ModelAdmin):
    pass 