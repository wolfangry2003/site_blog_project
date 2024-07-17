from django.db import models
from jalali_date import date2jalali

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    date = models.DateTimeField()
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')

    def __str__(self):
        return self.title
    def get_jalali_date(self):
        return date2jalali(self.date)

class Comment(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    date = models.DateTimeField()
    def __str__(self):
        return self.body

# Create your models here.
