from django.db import models
import datetime

class data(models.Model):
    category = models.CharField(max_length = 50)
    from_f = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    text = models.TextField()
    date = models.DateTimeField(null = True, default = datetime.datetime.now())
    idd = models.CharField(max_length=50)
    