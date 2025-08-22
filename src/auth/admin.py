# Dosya Adı: src/auth/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Admin panelinde görünecek alanları buraya ekleyebiliriz.
    # Şimdilik standart kalsın.

admin.site.register(CustomUser, CustomUserAdmin)