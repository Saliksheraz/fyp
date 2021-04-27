# Generated by Django 3.0.5 on 2021-01-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cell_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=100),
        ),
    ]