# Generated by Django 4.1.1 on 2023-04-04 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time_now',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='time_now',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='postlike',
            name='time_now',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tag',
            name='time_now',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='time_now',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
