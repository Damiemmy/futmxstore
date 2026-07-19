from django.contrib import admin
from apps.users.models import User,StudentProfile
# Register your models here.

class UserInfo(admin.ModelAdmin):
    list_display=['email','username','full_name']
    search_fields = ('full_name', 'reg_number', 'email')
    list_filter = ('is_active',)

class ProfileInfo(admin.ModelAdmin):
    list_display=['matric_number','level','user','department','faculty']
    search_fields = ('matric_number','email')
    list_filter = ('department',)


admin.site.register(User,UserInfo)
admin.site.register(StudentProfile,ProfileInfo)