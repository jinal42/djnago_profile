# Generated by Django 4.0.4 on 2022-04-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_alter_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('female', 'Female')], max_length=255)),
                ('hobby', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
