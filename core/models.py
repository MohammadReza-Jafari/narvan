from django.db import models


class Report(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    func_name = models.CharField(max_length=30)
    inputs = models.CharField(max_length=20)
    time_spent = models.FloatField()

    def __str__(self):
        return self.func_name
