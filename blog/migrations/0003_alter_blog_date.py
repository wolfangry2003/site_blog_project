# Generated by Django 5.0.7 on 2024-07-14 12:01

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=django_jalali.db.models.jDateField(),
        ),
    ]
