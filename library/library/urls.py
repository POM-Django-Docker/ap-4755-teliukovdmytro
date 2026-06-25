from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Адмін-панель
    path("admin/", admin.site.urls),

    # Документація API (Swagger)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Головні маршрути API v1 для всіх додатків
    path("api/v1/", include("author.api_urls")),
    path("api/v1/", include("book.api_urls")),
    path("api/v1/", include("order.api_urls")),
    path("api/v1/", include("authentication.api_urls")),
]
