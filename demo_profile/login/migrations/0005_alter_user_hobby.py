# Generated by Django 4.0.4 on 2022-04-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_user_hobby_alter_user_gender_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hobby',
            field=models.CharField(choices=[('reading', 'Reading'), ('dance', 'Dance'), ('drawing', 'Drawing')], default='dance', max_length=10),
        ),
    ]
