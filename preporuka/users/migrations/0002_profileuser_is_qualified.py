# Generated by Django 2.2.4 on 2019-08-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='is_qualified',
            field=models.BooleanField(default=False),
        ),
    ]
