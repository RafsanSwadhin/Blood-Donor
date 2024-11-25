# Generated by Django 5.1.2 on 2024-11-25 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_post_phone_number_post_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='details',
        ),
        migrations.AddField(
            model_name='post',
            name='alt_phone_number',
            field=models.CharField(blank=True, help_text='Enter alternative phone number in the format: +8801XXXXXXXXX', max_length=14, null=True, validators=[django.core.validators.RegexValidator('^\\+8801[3-9]\\d{8}$', 'Enter a valid Bangladeshi phone number.')]),
        ),
        migrations.AddField(
            model_name='post',
            name='say_something',
            field=models.TextField(blank=True, default='optional'),
        ),
    ]
