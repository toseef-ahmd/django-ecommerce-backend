# Generated by Django 3.0.5 on 2021-06-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, verbose_name='username'),
        ),
    ]