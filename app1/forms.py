from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Farmer, IncomeExpense, Farmer_User, FamilyMember, AssetLiability, BusinessInfo, LoanCredit


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Farmer_User
        fields = ['username', 'password']


# 基本信息
class FarmerInformationForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'


# 编辑基本信息
class FarmerEditForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )

    POLITICAL_STATUS_CHOICES = (
        ('群众', '群众'),
        ('团员', '团员'),
        ('党员', '党员'),
    )

    HEALTH_CONDITION_CHOICES = (
        ('健康', '健康'),
        ('亚健康', '亚健康'),
        ('不健康', '不健康'),
    )

    MARITAL_STATUS_CHOICES = (
        ('未婚', '未婚'),
        ('已婚', '已婚'),
        ('离异', '离异'),
    )

    EDUCATION_LEVEL_CHOICES = (
        ('小学', '小学'),
        ('初中', '初中'),
        ('高中', '高中'),
        ('大专', '大专'),
        ('本科', '本科'),
        ('硕士', '硕士'),
        ('博士', '博士'),
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    is_local_resident = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    political_status = forms.ChoiceField(choices=POLITICAL_STATUS_CHOICES,
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    health_condition = forms.ChoiceField(choices=HEALTH_CONDITION_CHOICES,
                                         widget=forms.Select(attrs={'class': 'form-control'}))
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES,
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    education_level = forms.ChoiceField(choices=EDUCATION_LEVEL_CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Farmer
        fields = '__all__'


# 家庭成员信息
class FamilyMemberForm(forms.ModelForm):
    RELATIONSHIP_CHOICES = [
        ('父母', '父母'),
        ('子女', '子女'),
        ('配偶', '配偶'),
        ('兄弟姐妹', '兄弟姐妹'),
        ('其他', '其他'),
    ]

    relationship = forms.ChoiceField(choices=RELATIONSHIP_CHOICES, label='与户主关系')

    class Meta:
        model = FamilyMember
        fields = ['name', 'relationship', 'id_number', 'contact']
        labels = {
            'name': '姓名',
            'id_number': '身份证号',
            'contact': '联系方式',
        }


# 填写家庭收支
class IncomeExpenseForm(forms.ModelForm):
    class Meta:
        model = IncomeExpense
        exclude = ['farmer']


# 填写资产负债
class AssetLiabilityForm(forms.ModelForm):
    class Meta:
        model = AssetLiability
        exclude = ['farmer']


# 填写经营信息
class BusinessInfoForm(forms.ModelForm):
    class Meta:
        model = BusinessInfo
        exclude = ['farmer']


# 贷款
class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanCredit
        fields = ['name', 'loan_amount']
