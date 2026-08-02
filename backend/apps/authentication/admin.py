from django.contrib import admin
from .models import User,Role,UserRole
# Register your models here.

class UserInfo(admin.ModelAdmin):
    list_display=['username','email']

admin.site.register(User,UserInfo)
admin.site.register(Role)
admin.site.register(UserRole)