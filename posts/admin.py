from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from posts.models import Post
from users.models import Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'user', 'photo')
    list_display_links = ('pk', 'user',)
    list_editable = ('title',)

    search_fields = (
        'title',
        'user__username'
    )

    list_filter = ("created", "modified")
    readonly_fields = ("created", "modified")

    fieldsets = (
        ("Post Info", {"fields": (("title", "photo", "created", "modified"))}),
        ("User info", {"fields": (("user", "profile"),)}),
    )
