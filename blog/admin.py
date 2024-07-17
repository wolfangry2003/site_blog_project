from django.contrib import admin
from .models import Blog, Comment
from django_jalali.admin.filters import JDateFieldListFilter


class BarAdmin(admin.ModelAdmin):
    list_filter = (
        ('date', JDateFieldListFilter),
    )


admin.site.register(Blog, BarAdmin)
admin.site.register(Comment)



