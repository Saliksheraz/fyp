# Generated by Django 3.1.7 on 2021-05-25 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrator', '0036_tasks_createdby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='loc',
        ),
        migrations.AddField(
            model_name='tasks',
            name='dateCreation',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='latitude',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='longitude',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='head',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
