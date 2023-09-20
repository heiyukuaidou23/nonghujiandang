"""shixun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app1 import views
from shixun import settings

urlpatterns = [
    path('admin/', admin.site.urls), # 银行经理
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name="home"),
    path('farmer_information/', views.farmer_information_view, name='information'),  # 填写个人信息
    # path('farmer/view/', views.view_farmer_information, name='view_farmer_information'), #查看个人信息
    path('farmer/<int:farmer_id>/edit/', views.edit_farmer_information, name='edit_farmer_information'),  # 编辑个人信息
    path('farmer/<int:farmer_id>/family_info/', views.fill_family_info, name='fill_family_info'),  # 填写家庭成员
    path('family/info/view/', views.view_family_info, name='view_family_info'),  # 查看家庭成员
    path('farmer/<int:family_id>/edit_info/', views.edit_family_info, name='edit_family_info'),  # 修改家庭信息
    path('family/<int:farmer_id>/finance/', views.add_family_finance, name='add_family_finance'),  # 填写家庭收支
    path('farmer/<int:farmer_id>/edit/income-expense/', views.edit_income_expense, name='edit_income_expense'),  # 修改家庭收支
    path('add/<int:farmer_id>/asset/liability/', views.add_asset_liability, name='add_asset_liability'),  # 填写资产负债情况
    path('edit/<int:farmer_id>/asset/liability/', views.edit_asset_liability, name='edit_asset_liability'),  # 修改资产负债情况
    path('add/<int:farmer_id>/business/info/', views.add_business_info, name='add_business_info'),  # 填写经营信息
    path('edit/<int:farmer_id>/business/info/', views.edit_business_info, name='edit_business_info'),  # 修改经营信息
    path('add/<int:farmer_id>/loan/', views.loan_application, name='loan_application'),  # 申请贷款
    path('view/loan/', views.view_loan, name="view_loan"),  # 查看审批情况
    path('farmer/list/', views.farmer_list),  # 功能列表
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
