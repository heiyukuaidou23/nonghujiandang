# Generated by Django 4.1.7 on 2023-06-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_farmer_password_remove_farmer_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
