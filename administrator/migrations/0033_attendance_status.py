# Generated by Django 3.1.7 on 2021-05-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0032_auto_20210524_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=100, null=True),
        ),
    ]
