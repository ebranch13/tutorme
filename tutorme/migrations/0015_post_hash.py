# Generated by Django 4.1.7 on 2023-03-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorme', '0014_post_creatorname'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hash',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
