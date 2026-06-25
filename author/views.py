from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'id'
