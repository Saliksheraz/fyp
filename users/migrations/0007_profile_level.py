# Generated by Django 3.0.5 on 2021-04-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.CharField(default='team_member', max_length=50, null=True),
        ),
    ]
