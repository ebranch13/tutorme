# Generated by Django 4.1.7 on 2023-03-18 21:17

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorme', '0010_remove_post_class_title_post_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='booked_sessions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None),
        ),
        migrations.AddField(
            model_name='post',
            name='capacity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='post',
            name='display_post',
            field=models.BooleanField(default=True),
        ),
    ]
