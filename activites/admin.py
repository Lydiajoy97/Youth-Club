from django.contrib import admin

# Register your models here.
@admin.register(ActivityForm)
class ActivityFormAdmin(admin.ModelAdmin):
    pass 