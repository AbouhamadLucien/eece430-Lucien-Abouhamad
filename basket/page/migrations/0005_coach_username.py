# Generated by Django 4.2 on 2023-04-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
