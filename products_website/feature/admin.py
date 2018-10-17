from django.contrib import admin

from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display =  [field.attname for field in Products._meta.fields]

class ProductAdmin(admin.ModelAdmin):
    list_display =  [field.attname for field in Products._meta.fields]

class Other_itemsAdmin(admin.ModelAdmin):
    list_display =  [field.attname for field in Other_items._meta.fields]

class OthersAdmin(admin.ModelAdmin):
    list_display =  [field.attname for field in Others._meta.fields]
class Dilivery_addressesAdmin(admin.ModelAdmin):
    list_display =  [field.attname for field in Dilivery_addresses._meta.fields]
class CustomersAdmin(admin.ModelAdmin):
    list_display =  [field.attname for field in Customers._meta.fields]
class CategoriesAdmin(admin.ModelAdmin):
    list_display =  [field.attname for field in Categories._meta.fields]

class LoginAdmin(admin.ModelAdmin):
    list_display =  [field.attname for field in Logins._meta.fields]



admin.site.register(Products,ProductAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Customers,CustomersAdmin)
admin.site.register(Dilivery_addresses,Dilivery_addressesAdmin)
admin.site.register(Others,OthersAdmin)
admin.site.register(Other_items,Other_itemsAdmin)
admin.site.register(Logins,LoginAdmin)