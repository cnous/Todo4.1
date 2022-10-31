from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "is_staff", "is_active", "is_superuser")
    list_filter = ("email", "is_active", "is_staff", "is_superuser")
    ordering = ("email",)
    searching_fields = ("email",)

    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("group_permissions", {"fields": ("groups", "user_permissions")}),
        ("important_date", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
