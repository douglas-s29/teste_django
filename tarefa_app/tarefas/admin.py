from django.contrib import admin
from .models import Task
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'user', 'data_criacao', 'inicio', 'fim')

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)