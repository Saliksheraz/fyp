# Generated by Django 3.0.5 on 2021-01-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='contact',
            new_name='mobile',
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='insta',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='secondName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.CharField(max_length=30, null=True),
        ),
    ]