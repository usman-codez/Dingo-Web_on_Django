from django.contrib import admin
from .models import Udata

# Register your models here.
@admin.register(Udata)
class Admin(admin.ModelAdmin):
    list_display = ['id','message','name','email','sub']