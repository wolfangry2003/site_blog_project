from django.db import models
from jalali_date import date2jalali
from django.urls import reverse
from django.utils import timezone
from datetime import date



class Blog(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    photo = models.ImageField()

    def __str__(self):
        return self.title

    def get_jalali_date(self):
        return date2jalali(self.date)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
# Create your models here.
