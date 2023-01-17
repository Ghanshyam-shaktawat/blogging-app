from django.contrib import admin
from .models import Post, Category
from django.utils.translation import ngettext
from django.contrib import messages

@admin.action(description='Make selection as Published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
    
@admin.action(description='Make selection as Draft')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')
    
@admin.action(description='Make selection as Taken Down')
def make_takendown(modeladmin, request, queryset):
    queryset.update(status='t')
    
@admin.action(description='Make as featured')
def featured(modeladmin, request, queryset):
    queryset.update(featured=True)
    
@admin.action(description='Remove as featured')
def non_featured(modeladmin, request, queryset):
    queryset.update(featured=False)
    

class PostAdmin(admin.ModelAdmin):
    list_display= ['title', 'author', 'pub_date','status', 'featured']
    ordering= ['-featured', '-pub_date']
    actions = [make_published, make_draft, make_takendown, featured, non_featured]
    search_fields= ['title', 'snippets']
    list_filter= ['status', 'featured', 'category']
    
    def has_add_permission(self, request):
        return False

admin.site.register(Post, PostAdmin)
admin.site.register(Category)