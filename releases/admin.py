from django.contrib import admin
from django.utils.html import format_html
from .models import Release, Image


class ReleaseImageInline(admin.StackedInline):
    model = Image
    max_num=10
    extra=0


class ReleaseAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['title', 'content']
    list_filter = ['created_at']
    inlines = [ReleaseImageInline]
    exclude = ['image_tag']

    def image_tag(self, obj):
        img_html = """
            <img src="{}" 
                onclick="window.open('{}', '_blank')"
                style="cursor:pointer;max-height:150px;max-width:150px;" />
        """
        try:
            if obj is not None and obj.show_image:
                return format_html(img_html.format(obj.show_image.url, obj.show_image.url))
            else:
                return 'No image available'
        except:
            return 'No image available'

    image_tag.short_description = 'Image'


admin.site.register(Release, ReleaseAdmin)