# Generated by Django 4.1.7 on 2023-06-21 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('id_number', models.CharField(max_length=18)),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('is_local_resident', models.BooleanField()),
                ('local_residence_years', models.IntegerField()),
                ('political_status', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('health_condition', models.CharField(max_length=255)),
                ('personal_qualities', models.CharField(max_length=255)),
                ('marital_status', models.CharField(max_length=255)),
                ('education_level', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LoanCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bank_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.bankmanager')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='IncomeExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labor_population', models.IntegerField()),
                ('dependent_population', models.IntegerField()),
                ('annual_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('operating_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expenditure', models.DecimalField(decimal_places=2, max_digits=10)),
                ('operating_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_expense', models.DecimalField(decimal_places=2, max_digits=10)),
                ('living_expense', models.DecimalField(decimal_places=2, max_digits=10)),
                ('farmer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='FarmerInformationAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField()),
                ('bank_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.bankmanager')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=255)),
                ('id_number', models.CharField(max_length=18)),
                ('contact', models.CharField(max_length=20)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessInformationApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField()),
                ('bank_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.bankmanager')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise_name', models.CharField(max_length=255)),
                ('production_cycle', models.CharField(max_length=255)),
                ('awards', models.CharField(max_length=255)),
                ('agricultural_subsidy', models.DecimalField(decimal_places=2, max_digits=10)),
                ('agricultural_insurance', models.BooleanField()),
                ('farmer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='AssetLiability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_count', models.IntegerField()),
                ('house_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('house_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car_count', models.IntegerField()),
                ('car_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('machinery_count', models.IntegerField()),
                ('machinery_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('farmer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.farmer')),
            ],
        ),
    ]
