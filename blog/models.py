from django.db import models
from jalali_date import date2jalali

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
    def get_jalali_date(self):
        return date2jalali(self.date)

# Create your models here.
