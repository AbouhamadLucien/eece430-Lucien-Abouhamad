# Generated by Django 4.2 on 2023-04-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_coach_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
