# Generated by Django 4.0.4 on 2022-04-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='male', max_length=20),
        ),
    ]
