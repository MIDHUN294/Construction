# Generated by Django 3.1.6 on 2021-02-07 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appLabour', '0018_auto_20210207_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='EducationalQalifications',
            new_name='EducationalQualifications',
        ),
    ]
