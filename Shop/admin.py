from django.contrib import admin


from Shop.models import Header


# Register your models here.
@admin.register(Header)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('mobile_name', 'mobile_name_fa')