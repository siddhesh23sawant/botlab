# Generated by Django 3.1.2 on 2020-10-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=True),
        ),
    ]
