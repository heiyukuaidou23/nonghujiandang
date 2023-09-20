from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from . import models
from .forms import RegistrationForm, LoginForm, FarmerInformationForm, FarmerEditForm, FamilyMemberForm, \
    IncomeExpenseForm, AssetLiabilityForm, BusinessInfoForm, LoanApplicationForm
from .models import Farmer, FamilyMember, IncomeExpense, AssetLiability, BusinessInfo, LoanCredit


# 注册
def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


# 登录
def user_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {'form': form})
    form = LoginForm(data=request.POST)
    if not form.is_valid():
        return render(request, "login.html", {'form': form})
    user = form.cleaned_data['username']
    pwd = form.cleaned_data['password']
    user_object = models.Farmer_User.objects.filter(username=user, password=pwd).first()
    if not user_object:
        return render(request, "login.html", {'form': form, 'error': "用户名或密码错误"})
    request.session['info'] = {"id": user_object.id, 'name': user_object.username}
    # 设置一个时间为一周
    request.session.set_expiry(60 * 60 * 24 * 7)
    return redirect('home')

#主页面
def home(request):
    if 'info' in request.session:
        # 用户已登录，隐藏登录与注册按钮
        show_login_register = False
    else:
        # 用户未登录，显示登录与注册按钮
        show_login_register = True
    return render(request, "home.html", {'show_login_register': show_login_register})

# 退出
def user_logout(request):
    logout(request)
    return redirect('home')  # 注销成功后重定向到主页面


# 填写个人信息
def farmer_information_view(request):
    if request.method == 'POST':
        form = FarmerInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FarmerInformationForm()
    return render(request, 'farmer_information.html', {'form': form})


# 修改个人信息
def edit_farmer_information(request, farmer_id):
    farmer = get_object_or_404(Farmer, pk=farmer_id)
    if request.method == 'POST':
        form = FarmerEditForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FarmerEditForm(instance=farmer)
    context = {'form': form, 'farmer': farmer}
    return render(request, 'edit_farmer.html', context)

#个人信息界面
def farmer_list(request):
    return render(request, 'farmer_list.html')


# 填写家庭信息
def fill_family_info(request, farmer_id):
    farmer = get_object_or_404(Farmer, pk=farmer_id)
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST)
        if form.is_valid():
            family_member = form.save(commit=False)
            family_member.farmer = farmer
            family_member.save()
            return redirect('home')
    else:
        form = FamilyMemberForm()
    context = {'form': form}
    return render(request, 'fill_family_info.html', context)


# 查询家庭信息
def view_family_info(request):
    families = FamilyMember.objects.all()
    context = {'families': families}
    return render(request, 'view_family_info.html', context)


# 修改家庭信息
def edit_family_info(request, family_id):
    family = get_object_or_404(FamilyMember, pk=family_id)
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST, instance=family)
        if form.is_valid():
            form.save()
            return redirect('view_family_info')
    else:
        form = FamilyMemberForm(instance=family)

    context = {'form': form, 'family': family}
    return render(request, 'edit_family_info.html', context)


# 填写家庭收支
def add_family_finance(request, farmer_id):
    farmer = get_object_or_404(Farmer, pk=farmer_id)

    if request.method == 'POST':
        form = IncomeExpenseForm(request.POST)
        if form.is_valid():
            finance = form.save(commit=False)
            finance.farmer = farmer
            finance.save()
            return redirect('home', farmer_id=farmer_id)
    else:
        form = IncomeExpenseForm()

    context = {'farmer': farmer, 'form': form}
    return render(request, 'add_family_finance.html', context)


# 修改家庭收支
def edit_income_expense(request, farmer_id):
    farmer = get_object_or_404(Farmer, pk=farmer_id)
    income_expense, created = IncomeExpense.objects.get_or_create(farmer=farmer)

    if request.method == 'POST':
        form = IncomeExpenseForm(request.POST, instance=income_expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncomeExpenseForm(instance=income_expense)

    context = {'form': form, 'farmer': farmer}
    return render(request, 'edit_income_expense.html', context)


# 填写资产负债情况
def add_asset_liability(request, farmer_id):
    farmer = get_object_or_404(Farmer, pk=farmer_id)
    if request.method == 'POST':
        form = AssetLiabilityForm(request.POST, request.FILES)
        if form.is_valid():
            asset_liability = form.save(commit=False)
            asset_liability.farmer = farmer
            asset_liability.save()
            return redirect('home')
    else:
        form = AssetLiabilityForm()

    context = {'form': form}
    return render(request, 'add_asset_liability.html', context)


# 修改资产负债情况
def edit_asset_liability(request, farmer_id):
    farmer = get_object_or_404(Farmer, pk=farmer_id)
    asset_liability = get_object_or_404(AssetLiability, farmer=farmer)

    if request.method == 'POST':
        form = AssetLiabilityForm(request.POST, request.FILES, instance=asset_liability)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AssetLiabilityForm(instance=asset_liability)

    context = {'form': form, 'farmer': farmer}
    return render(request, 'edit_asset_liability.html', context)

# 填写经营信息
def add_business_info(request, farmer_id):
    farmer = get_object_or_404(Farmer, id=farmer_id)
    if request.method == 'POST':
        form = BusinessInfoForm(request.POST, request.FILES)
        if form.is_valid():
            business_info = form.save(commit=False)
            business_info.farmer = farmer
            business_info.save()
            return redirect('home', farmer_id=farmer_id)
    else:
        form = BusinessInfoForm()
    context = {
        'form': form,
        'farmer_id': farmer_id,
    }
    return render(request, 'add_business_info.html', context)

# 修改经营信息
def edit_business_info(request, farmer_id):
    farmer = get_object_or_404(Farmer, id=farmer_id)
    try:
        business_info = BusinessInfo.objects.get(farmer=farmer)
    except BusinessInfo.DoesNotExist:
        business_info = None
    if request.method == 'POST':
        form = BusinessInfoForm(request.POST, request.FILES, instance=business_info)
        if form.is_valid():
            business_info = form.save(commit=False)
            business_info.farmer = farmer
            business_info.save()
            return redirect('home')
    else:
        form = BusinessInfoForm(instance=business_info)

    context = {
        'form': form,
        'farmer_id': farmer_id,
    }
    return render(request, 'edit_business_info.html', context)

# 贷款授信
def loan_application(request, farmer_id):
    farmer = get_object_or_404(Farmer, id=farmer_id)
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            loan_info = form.save(commit=False)
            loan_info.farmer = farmer
            loan_info.save()
            return redirect('home')
    else:
        form = LoanApplicationForm()
    context = {
        'form': form,
        'farmer_id': farmer_id,
    }
    return render(request, 'add_loan.html', context)

# 查看审批情况
def view_loan(request):
    loans = LoanCredit.objects.all()
    context = {'loans': loans}
    return render(request, 'view_loan.html', context)

