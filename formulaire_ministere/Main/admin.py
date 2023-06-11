from django.contrib import admin

from .models import *
from django.contrib.auth.admin import UserAdmin



# Register your models here.


class DataFormAdmin(admin.ModelAdmin):
    list_display = ('detenteur','lieu_extraction','commune','substence','montant','date')


class CustomAdmin(UserAdmin):
    list_display = ('username','password')    

admin.site.register(DataForm, DataFormAdmin)

admin.site.register(CustomUser,CustomAdmin)








