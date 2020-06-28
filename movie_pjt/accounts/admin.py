from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)

class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets[1][1]['fields']+=('nickname', 'introduction')
    UserAdmin.add_fieldsets +=(
        (('Additional Info'), {'fields':('nickname', 'introduction')})
    )