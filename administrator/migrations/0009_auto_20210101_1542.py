# Generated by Django 3.0.5 on 2021-01-01 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0008_auto_20210101_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensordata',
            old_name='date',
            new_name='timeStamp',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='time',
        ),
    ]
