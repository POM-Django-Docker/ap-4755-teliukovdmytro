from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        # Фільтруємо замовлення, якщо в URL передано ID користувача
        if 'user_pk' in self.kwargs:
            return Order.objects.filter(user_id=self.kwargs['user_pk'])
        return Order.objects.all()
