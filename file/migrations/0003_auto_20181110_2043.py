# Generated by Django 2.1.1 on 2018-11-10 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20181110_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectfiles',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True),
        ),
    ]
