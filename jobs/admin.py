from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'city', 'created_at')
    list_filter = ('category', 'city')
    search_fields = ('title', 'skills_required', 'city')
