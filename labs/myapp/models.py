from django.db import models

class User(models.Model):
    id = models.CharField(max_length=64, primary_key=True, unique=True)
    real_name = models.CharField(max_length=64)
    tz = models.CharField(max_length=64)

    def __str__(self):
        return self.real_name
        
    # @property
    # def activity_periods(self):
    #     return self.activityperiod_set.all()

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, related_name='activity_periods', on_delete=models.CASCADE, default='DEFAULT VALUE')
    start_time = models.CharField(max_length=64)
    end_time = models.CharField(max_length=64)
