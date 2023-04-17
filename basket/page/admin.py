from django.contrib import admin
from .models import User, Coach

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name', 'phone_number', 'email', 'gender', 'skill_level')
    actions = ['delete_selected']
admin.site.register(User, UserAdmin)

class CoachAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name', 'phone_number', 'email', 'gender', 'experience', 'resume')
    actions = ['delete_selected']
admin.site.register(Coach, CoachAdmin)
