from django.contrib import admin
from .forms import RegisterForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from main.models import Post
from django.db.models import Count
from django.db.models import Q

class CustomUserAdmin(admin.ModelAdmin):
    ordering= ['username']
    list_display = ['username', 'email', 'first_name', 'last_name', 'last_login', 'is_active', 'get_post_count']
    search_fields= ['email', 'username']
    list_filter= ['is_active']
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_image' ,'username', 'email', 'first_name', 'last_name', 'about', 'last_login', 'is_staff', 'is_active', 'user_permissions')}
        ),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(post_count=Count('posts'))
    
    def get_post_count(self, obj):
        return obj.post_count
    
    get_post_count.short_description = "post published"
    
    
admin.site.register(CustomUser, CustomUserAdmin) 