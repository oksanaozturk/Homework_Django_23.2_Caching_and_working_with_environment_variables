from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Класс для регистрации публикации в админке."""
    list_display = ('id', 'title', 'slug', 'date_of_creation', 'is_published', 'view_counter')
    list_filter = ('date_of_creation',)
    search_fields = ('title', 'is_published',)
    prepopulated_fields = {"slug": ("title",)}
