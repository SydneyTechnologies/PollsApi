from django.contrib import admin 
from .models import MyUser
# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyUser, MyUserAdmin)