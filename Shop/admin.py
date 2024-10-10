from django.contrib import admin

import Shop
from Shop.models import Header, Mobile, Brands, Categories, Mobile_Network


# Register your models here.
@admin.register(Header)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('mobile_name', 'mobile_name_fa')


@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Name_fa' , 'Slug')


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ['Brand_Name' , 'slug']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['Category_Name' , 'Category_Slug']


@admin.register(Mobile_Network)
class Mobile_NetworkAdmin(admin.ModelAdmin):
    list_display = ['Networks']
