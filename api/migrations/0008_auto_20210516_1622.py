# Generated by Django 3.0.5 on 2021-05-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210515_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='sample.jpg', null=True, upload_to=''),
        ),
    ]
