from django.contrib import admin
from .models import Release, ReleaseImage


class ReleaseImageInline(admin.StackedInline):
    model = ReleaseImage
    max_num=10
    extra=0


class ReleaseAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['title', 'content']
    list_filter = ['created_at']
    inlines = [ReleaseImageInline]

admin.site.register(Release, ReleaseAdmin)