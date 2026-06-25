from django.urls import path
from .views import AuthorListCreateAPIView, AuthorDetailAPIView

urlpatterns = [
    path('author/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('author/<int:id>/', AuthorDetailAPIView.as_view(), name='author-detail'),
]
