# Generated by Django 3.1.6 on 2021-02-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLabour', '0029_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='Price',
            field=models.IntegerField(max_length=100),
        ),
    ]