# Generated by Django 3.1.2 on 2020-11-01 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='images',
            field=models.ImageField(upload_to='skill/'),
        ),
    ]