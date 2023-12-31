# Generated by Django 2.2.28 on 2023-09-07 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_alter_loancredit_options_remove_farmer_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetliability',
            name='farmer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.Farmer', verbose_name='户主姓名'),
        ),
        migrations.AlterField(
            model_name='assetliability',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='assetliability',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='图片附件'),
        ),
        migrations.AlterField(
            model_name='businessinfo',
            name='farmer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.Farmer', verbose_name='户主姓名'),
        ),
        migrations.AlterField(
            model_name='businessinfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Farmer', verbose_name='户主姓名'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='farmer_user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='farmer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.Farmer', verbose_name='户主姓名'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='loancredit',
            name='farmer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.Farmer', verbose_name='户主姓名'),
        ),
        migrations.AlterField(
            model_name='loancredit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
