from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user', 'created_at', 'plated_end_at', 'end_at')
    list_filter = ('book__id', 'book__name', 'book__authors', 'created_at', 'end_at')
    search_fields = ('book__name', 'user__email')

    readonly_fields = ('created_at',)

    fieldsets = (
        ('Основна інформація', {
            'fields': ('book', 'user', 'created_at')
        }),
        ('Дати видачі та повернення', {
            'fields': ('plated_end_at', 'end_at')
        }),
    )
