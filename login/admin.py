from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from login.models import CustomUser, UserPasswords
from login.forms import CustomUserChangeForm


@admin.register(UserPasswords)
class UserPasswordsAdmin(admin.ModelAdmin):
    list_display = ('user', 'password')


# class CustomAdmin(UserAdmin):
#     form = CustomUserChangeForm
#     model = CustomUser

#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         (("Personal info"), {"fields": ("first_name", "last_name", "role")}),
#         (
#             ("Permissions"),
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 ),
#             },
#         ),
#         (("Important dates"), {"fields": ("last_login", "date_joined", "last_change_password")}),
#     )
    
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("email", "password1", "password2"),
#             },
#         ),
#     )
#     list_display = ("email", "first_name", "last_name", "is_staff")
#     list_filter = ("is_staff", "is_superuser", "is_active", "groups")
#     search_fields = ("first_name", "last_name", "email")
#     ordering = ("email",)
#     filter_horizontal = (
#         "groups",
#         "user_permissions",
#     )

admin.site.register(CustomUser)
