from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    search_fields = ('name', 'surname')

    fieldsets = (
        ('Особисті дані', {
            'fields': ('name', 'surname', 'patronymic')
        }),
    )
