from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView

urlpatterns = [
    path('book/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('book/<int:id>/', BookDetailAPIView.as_view(), name='book-detail'),
]
