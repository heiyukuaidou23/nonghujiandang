from django.db import models

from django.db import models

class Farmer_User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(verbose_name='Last Login', blank=True, null=True)


# 个人信息表
class Farmer(models.Model):
    name = models.CharField(max_length=255, verbose_name='户主姓名')
    id_number = models.CharField(max_length=18, verbose_name='身份证号')
    gender = models.CharField(max_length=10, verbose_name='性别')
    phone_number = models.CharField(max_length=20, verbose_name='手机号码')
    is_local_resident = models.BooleanField(verbose_name='本地常住')
    local_residence_years = models.IntegerField(verbose_name='本地居住年限')
    political_status = models.CharField(max_length=255, verbose_name='政治面貌')
    occupation = models.CharField(max_length=255, verbose_name='个人职业')
    health_condition = models.CharField(max_length=255, verbose_name='健康状况')
    personal_qualities = models.CharField(max_length=255, verbose_name='个人品质')
    marital_status = models.CharField(max_length=255, verbose_name='婚姻状况')
    education_level = models.CharField(max_length=255, verbose_name='文化程度')
    region = models.CharField(max_length=255, verbose_name='所属区域')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "基本信息表"
        verbose_name_plural = "基本信息"


# 家庭成员信息
class FamilyMember(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE,verbose_name="户主姓名")
    name = models.CharField(max_length=255, verbose_name="姓名")  # 姓名
    relationship = models.CharField(max_length=255, verbose_name='与户主关系')  # 与户主关系
    id_number = models.CharField(max_length=18, verbose_name='身份证号')  # 身份证号
    contact = models.CharField(max_length=20, verbose_name='联系方式')  # 联系方式

    class Meta:
        verbose_name = "家庭信息表"
        verbose_name_plural = "家庭信息"


# 资产负债情况
class AssetLiability(models.Model):
    farmer = models.OneToOneField(Farmer, on_delete=models.CASCADE,verbose_name="户主姓名")
    house_count = models.IntegerField(verbose_name='农房套数')
    house_area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='面积')
    house_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='农房价值')
    car_count = models.IntegerField(verbose_name='汽车数量')
    car_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='汽车价值')
    machinery_count = models.IntegerField(verbose_name='农用机械数量')
    machinery_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='农用机械价值')
    image = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name='图片附件')  # 图片附件字段

    def __str__(self):
        return str(self.farmer)

    class Meta:
        verbose_name = "资产负债情况"
        verbose_name_plural = "资产负债情况"


# 家庭收支信息
class IncomeExpense(models.Model):
    farmer = models.OneToOneField(Farmer, on_delete=models.CASCADE,verbose_name="户主姓名")
    labor_population = models.IntegerField(verbose_name='劳动人口')
    dependent_population = models.IntegerField(verbose_name='供养人口')
    annual_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='家庭年收入')
    operating_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='经营收入总和')
    other_income = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='其他收入')
    expenditure = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='家庭支出')
    operating_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='经营成本')
    tax_expense = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='税费支出总和')
    living_expense = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='生活支出')

    class Meta:
        verbose_name = "家庭收支信息"
        verbose_name_plural = "家庭收支信息"


# 经营信息
class BusinessInfo(models.Model):
    farmer = models.OneToOneField(Farmer, on_delete=models.CASCADE,verbose_name="户主姓名")
    enterprise_name = models.CharField(max_length=255, verbose_name='企业名称')
    production_cycle = models.CharField(max_length=255, verbose_name='生产经营周期')
    awards = models.CharField(max_length=255, verbose_name='获奖情况')
    agricultural_subsidy = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='农业补贴（元/年）')
    agricultural_insurance = models.BooleanField(verbose_name='是否参保农业保险')
    business_license = models.ImageField(upload_to='business/licenses/', null=True, blank=True, verbose_name='营业执照')

    class Meta:
        verbose_name = "经营信息"
        verbose_name_plural = "经营信息"


# 贷款授信
class LoanCredit(models.Model):
    STATUS_CHOICES = [
        ('pending', '待审核'),
        ('approved', '已通过'),
        ('rejected', '未通过'),
    ]

    farmer = models.OneToOneField(Farmer, on_delete=models.CASCADE,verbose_name="户主姓名")
    name = models.CharField(max_length=255, verbose_name="姓名")  # 姓名
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='审核状态')
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='贷款金额')

    class Meta:
        verbose_name = "最终审核"
        verbose_name_plural = "最终审核"


def __str__(self):
    return self.username
