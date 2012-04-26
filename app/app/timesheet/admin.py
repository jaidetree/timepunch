from app.timesheet.models import TimeEntry
from django.contrib import admin

class TimeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(TimeEntry, TimeAdmin) 
