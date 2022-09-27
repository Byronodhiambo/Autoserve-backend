from django.contrib import admin
from .models import Productmaster, Subgroupmaster, Productgroupmaster, Departmentmaster
from django.contrib.auth.models import Group
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'productname', 'subgroupid', 'productgroupid', 'departmentid', 'picture1', 'picture2', 'price', 'trial_standardcostprice_28']
    list_filter = ['productgroupid', 'departmentid']

class SubgroupmasterAdmin(admin.ModelAdmin):
    list_display = ['subgroupid', 'subgroupname','productgroupid']

class ProductgroupAdmin(admin.ModelAdmin):
    list_display = ['trial_productgroupid_1', 'productgroupname', 'departmentid']
    list_filter = ['departmentid']

class DepartmentmasterAdmin(admin.ModelAdmin):
    list_display = ['departmentid', 'departmentname']



admin.site.site_header = "Product admin"
admin.site.register(Productmaster, ProductAdmin)
admin.site.register(Subgroupmaster, SubgroupmasterAdmin)
admin.site.register(Productgroupmaster, ProductgroupAdmin)
admin.site.register(Departmentmaster,DepartmentmasterAdmin)
admin.site.unregister(Group)
