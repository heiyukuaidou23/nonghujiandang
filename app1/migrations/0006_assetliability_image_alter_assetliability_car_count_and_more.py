# Generated by Django 4.1.7 on 2023-06-23 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_farmer_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetliability',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/'),
        ),
        migrations.AlterField(
            model_name='assetliability',
            name='car_count',
            field=models.IntegerField(verbose_name='汽车数量'),
        ),
        migrations.AlterField(
            model_name='assetliability',
            name='car_value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='汽车价值'),
        ),
        migrations.AlterField(
            model_name='assetliability',
            name='house_area',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='面积'),
        ),
        migrations.AlterField(
            model_name='assetliability',
            name='house_count',
            field=models.IntegerField(verbose_name='农房套数'),
        ),
        migrations.AlterField(
            model_name='assetliability',
            name='house_value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='农房价值'),
        ),
        migrations.AlterField(
            model_name='assetliability',
            name='machinery_count',
            field=models.IntegerField(verbose_name='农用机械数量'),
        ),
        migrations.AlterField(
            model_name='assetliability',
            name='machinery_value',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='农用机械价值'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='education_level',
            field=models.CharField(max_length=255, verbose_name='文化程度'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='gender',
            field=models.CharField(max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='health_condition',
            field=models.CharField(max_length=255, verbose_name='健康状况'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='id_number',
            field=models.CharField(max_length=18, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='is_local_resident',
            field=models.BooleanField(verbose_name='本地常住'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='local_residence_years',
            field=models.IntegerField(verbose_name='本地居住年限'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='marital_status',
            field=models.CharField(max_length=255, verbose_name='婚姻状况'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='name',
            field=models.CharField(max_length=255, verbose_name='户主姓名'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='occupation',
            field=models.CharField(max_length=255, verbose_name='个人职业'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='personal_qualities',
            field=models.CharField(max_length=255, verbose_name='个人品质'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='phone_number',
            field=models.CharField(max_length=20, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='political_status',
            field=models.CharField(max_length=255, verbose_name='政治面貌'),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='region',
            field=models.CharField(max_length=255, verbose_name='所属区域'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='annual_income',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='家庭年收入'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='dependent_population',
            field=models.IntegerField(verbose_name='供养人口'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='expenditure',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='家庭支出'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='labor_population',
            field=models.IntegerField(verbose_name='劳动人口'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='living_expense',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='生活支出'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='operating_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='经营成本'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='operating_income',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='经营收入总和'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='other_income',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='其他收入'),
        ),
        migrations.AlterField(
            model_name='incomeexpense',
            name='tax_expense',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='税费支出总和'),
        ),
    ]
