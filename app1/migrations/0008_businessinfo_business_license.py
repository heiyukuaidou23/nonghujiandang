# Generated by Django 4.1.7 on 2023-06-25 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_assetliability_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinfo',
            name='business_license',
            field=models.ImageField(blank=True, null=True, upload_to='business/licenses/', verbose_name='图片'),
        ),
    ]
