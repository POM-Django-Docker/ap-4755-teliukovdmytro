from django.urls import path, include
from rest_framework_nested import routers
from authentication.views import UserViewSet
from .views import OrderViewSet

# Базовий роутер
router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')

# Вкладений роутер для замовлень користувача: /api/v1/user/{id}/order/
user_router = routers.NestedSimpleRouter(router, r'user', lookup='user')
user_router.register(r'order', OrderViewSet, basename='user-orders')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(user_router.urls)),
]
