# Generated by Django 3.2.17 on 2023-02-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorme', '0002_auto_20230222_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='name',
        ),
        migrations.AddField(
            model_name='tutee',
            name='first_name',
            field=models.CharField(default='first_name', max_length=150),
        ),
        migrations.AddField(
            model_name='tutee',
            name='last_name',
            field=models.CharField(default='last_name', max_length=150),
        ),
        migrations.AddField(
            model_name='tutee',
            name='username',
            field=models.CharField(default='username', max_length=150),
        ),
        migrations.AddField(
            model_name='tutor',
            name='first_name',
            field=models.CharField(default='first_name', max_length=150),
        ),
        migrations.AddField(
            model_name='tutor',
            name='last_name',
            field=models.CharField(default='last_name', max_length=150),
        ),
        migrations.AddField(
            model_name='tutor',
            name='username',
            field=models.CharField(default='username', max_length=150),
        ),
        migrations.AlterField(
            model_name='tutee',
            name='email',
            field=models.CharField(default='email', max_length=150),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='email',
            field=models.CharField(default='email', max_length=150),
        ),
    ]
