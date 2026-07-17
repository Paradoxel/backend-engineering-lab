from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User,Profile

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ("-created_date",)
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    search_fields = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
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
                ),
            },
        ),
    )



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "first_name",
        "last_name",
        "created_date",
    )

    search_fields = (
        "user__email",
        "first_name",
        "last_name",
    )

    ordering = (
        "-created_date",
    )

    list_filter = (
        "created_date",
    )