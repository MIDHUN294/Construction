# Generated by Django 3.1.6 on 2021-02-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLabour', '0026_remove_sample_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='ConfirmPassword',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Password',
            field=models.CharField(max_length=8),
        ),
    ]
