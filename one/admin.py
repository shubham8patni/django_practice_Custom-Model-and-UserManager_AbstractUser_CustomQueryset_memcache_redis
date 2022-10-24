from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
# Register your models here.


class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ('email', 'username', 'is_staff', 'is_active')
    fieldsets = (
        ('User Info', {'fields': ('email', 'password', 'gender')}),
        ('Dates', {'fields': ('birthday', 'last_login', 'date_joined')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(MyUser ,MyUserAdmin)