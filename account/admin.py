#coding:utf-8
from django.contrib import admin
from .forms import MyUserChangeForm, MyUserCreationForm
from django.contrib.auth.admin import UserAdmin
from account.models import User, Group
from account.models import Permission
# Register your models here.
class MyUserAdmin(UserAdmin):
# The forms to add and change user instances
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    # The fields to be used in displaying the User model.
    fieldsets = (
        (None, {'fields': ('uid','uname','ugroup','password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups','upermission')}),
#         ('Important dates', {'fields': ('qq_name', 'type', 'level', 'profile', 'with_total','accu_income', 'date_joined', )}),
#         ('others', {'fields': ('balance', 'margin_account','domain_name', 'cs_qq', 'invite_code', 'inviter','zhifubao')}),
    )
    add_fieldsets = (
    (None, {
            'classes': ('wide',),
            'fields': ('uid','uname','uqq','password1', 'password2')}
            ),
    )
    search_fields = ('uid','uname','uqq')
    ordering = ('uid',)
    list_display = ('uid','uname','uqq','ujointime','uleavetime','uremarks','urecord','is_staff','is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    filter_horizontal = ('upermission',)
# Now register the new UserAdmin...
admin.site.register(User,MyUserAdmin)

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('desc','modulename')
    search_fields = ['modulename',]
admin.site.register(Permission,PermissionAdmin)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('gname','id')
    search_fields = ['gname',]
admin.site.register(Group,GroupAdmin)