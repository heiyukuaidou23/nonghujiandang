# Generated by Django 4.1.7 on 2023-06-26 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_loancredit_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loancredit',
            options={'verbose_name': '最终审核', 'verbose_name_plural': '最终审核'},
        ),
        migrations.RemoveField(
            model_name='farmer',
            name='status',
        ),
        migrations.AlterField(
            model_name='loancredit',
            name='status',
            field=models.CharField(choices=[('pending', '待审核'), ('approved', '已通过'), ('rejected', '未通过')], default='pending', max_length=20, verbose_name='审核状态'),
        ),
    ]
