from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('text', 'link', 'link_text')
    search_fields = ('text', 'link', 'link_text')

admin.site.register(Content, ContentAdmin)
