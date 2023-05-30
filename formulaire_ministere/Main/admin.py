from django.contrib import admin

from .models import *
from django.contrib.auth.admin import UserAdmin



# Register your models here.


class DataFormAdmin(admin.ModelAdmin):
    list_display = ('detenteur','lieu_extraction','commune','substence','montant','date')

admin.site.register(DataForm, DataFormAdmin)

admin.site.register(FullUser)

admin.site.register(Staff)







