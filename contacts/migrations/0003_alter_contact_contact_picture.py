# Generated by Django 3.2.9 on 2021-11-23 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20211123_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_picture',
            field=models.URLField(null=True),
        ),
    ]
