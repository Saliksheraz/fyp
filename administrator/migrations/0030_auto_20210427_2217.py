# Generated by Django 3.0.5 on 2021-04-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0029_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='sub',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]