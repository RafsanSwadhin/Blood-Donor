# Generated by Django 5.1.2 on 2024-11-25 12:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phone_number',
            field=models.CharField(default='+8801000000000', help_text='Enter phone number in the format: +8801XXXXXXXXX', max_length=14, validators=[django.core.validators.RegexValidator('^\\+8801[3-9]\\d{8}$', 'Enter a valid Bangladeshi phone number.')]),
        ),
        migrations.AddField(
            model_name='post',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10),
        ),
    ]