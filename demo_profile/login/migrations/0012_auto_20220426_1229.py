# Generated by Django 3.1 on 2022-04-26 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_user1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user1',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
