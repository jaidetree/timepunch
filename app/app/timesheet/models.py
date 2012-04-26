from django.db import models
from django.contrib.auth.models import User
import math

class TimeEntry(models.Model):
    start_time = models.DateTimeField(blank=False)
    stop_time = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, null=True) 

    class Meta:
        ordering = ['-start_time']
        verbose_name_plural = "time entries"
    
    def __unicode__(self):
        return str(self.id)

    def hours(self):
        if not self.stop_time:
            return None
        else:
            time = self.stop_time - self.start_time
            seconds = time.total_seconds()
            days = time.days
            seconds = seconds - ( 60 * 3600 * days )
            hours = int(seconds / 3600)
            seconds = seconds - ( hours * 3600 )
            minutes = int(seconds / 60)
            if hours > 0:
                return str(int(hours + round(seconds / 60 ) / 60)) + " hours"
            seconds = seconds - ( minutes * 60 )

            return "{}:{}".format(minutes, int(seconds))
    def seconds(self):
        if not self.stop_time:
            return 0
        else:
            time = self.start_time()
            return time.total_seconds()
