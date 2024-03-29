# Generated by Django 3.0.5 on 2021-04-27 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0028_auto_20210427_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('loc', models.CharField(blank=True, max_length=200, null=True)),
                ('loc_name', models.CharField(blank=True, max_length=200, null=True)),
                ('sub', models.CharField(blank=True, max_length=200, null=True)),
                ('feedback', models.CharField(blank=True, max_length=200, null=True)),
                ('datetime', models.DateTimeField(auto_now=True, null=True)),
                ('desc', models.TextField(null=True, verbose_name='Description')),
                ('Team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.Team')),
            ],
        ),
    ]
