from django.contrib import admin

from .models import Farmer, FamilyMember, AssetLiability, IncomeExpense, BusinessInfo, LoanCredit

admin.site.site_header = '银行经理登录端'
admin.site.site_title = '银行经理管理后台'
admin.site.index_title = '银行经理管理后台'


# 个人信息
@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'id_number')
    readonly_fields = ('name', 'id_number', 'gender', 'phone_number', 'is_local_resident', 'local_residence_years',
                       'political_status', 'occupation', 'health_condition', 'personal_qualities', 'marital_status',
                       'education_level', 'region')


# 家庭信息
@admin.register(FamilyMember)
class FamilyMember(admin.ModelAdmin):
    list_display = ('name', 'contact')
    exclude = ['farmer']
    readonly_fields = [f.name for f in FamilyMember._meta.get_fields()]


# 资产负债情况
@admin.register(AssetLiability)
class AssetLiability(admin.ModelAdmin):
    list_display = ('house_count', 'house_area', 'house_value')
    exclude = ['farmer']
    readonly_fields = [f.name for f in AssetLiability._meta.get_fields()]


# 家庭收支信息
@admin.register(IncomeExpense)
class IncomeExpense(admin.ModelAdmin):
    list_display = ('labor_population', 'annual_income', 'expenditure')
    exclude = ['farmer']
    readonly_fields = [f.name for f in IncomeExpense._meta.get_fields()]


@admin.register(BusinessInfo)
class BusinessInfo(admin.ModelAdmin):
    list_display = ('enterprise_name', 'production_cycle', 'agricultural_subsidy')
    exclude = ['farmer']
    readonly_fields = [f.name for f in BusinessInfo._meta.get_fields()]


@admin.register(LoanCredit)
class LoanCreditAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'loan_amount')
    list_filter = ('status',)
    fields = ['farmer', 'name', 'loan_amount', 'status']
    readonly_fields = ['name', 'farmer']
    actions = ['approve_loans', 'reject_loans']

    def approve_loans(self, request, queryset):
        if request.user.is_superuser:
            queryset.update(status='approved')

    def reject_loans(self, request, queryset):
        if request.user.is_superuser:
            queryset.update(status='rejected')

    approve_loans.short_description = '批准所选农户'
    reject_loans.short_description = '拒绝所选农户'
