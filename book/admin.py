from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_authors', 'count')
    list_filter = ('authors',)
    search_fields = ('id', 'name', 'authors__name', 'authors__surname')

    fieldsets = (
        ('Незмінні дані', {
            'fields': ('name', 'description', 'authors')
        }),
        ('Змінні дані', {
            'fields': ('count',)
        }),
    )

    def get_authors(self, obj):
        return ", ".join([f"{a.name} {a.surname}" for a in obj.authors.all()])

    get_authors.short_description = 'Автори'
