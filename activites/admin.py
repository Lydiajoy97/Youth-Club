from django.contrib import admin
from .models import ActivityForm

# Register your models here.
@admin.register(ActivityForm)
class ActivityFormAdmin(admin.ModelAdmin):
    list_display = ('author', 'status', 'game_ideas')