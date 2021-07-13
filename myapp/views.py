from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from myapp.models import Book, Borrow
from myapp.serializers import BookSerializer, WriteBorrowSerializer, ReadBorrowSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Create your views here.
class BookModelViewset(ModelViewSet):
    authentication_classes = (TokenAuthentication,) 
    queryset =  Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = None


class BorrowModelViewset(ModelViewSet):
    authentication_classes = (TokenAuthentication,) 

    def get_queryset(self):
        return Borrow.objects.select_related("book", "user").filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrive"):
            return ReadBorrowSerializer
        return WriteBorrowSerializer

    
class UserRegisterModelViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    pagination_class = None



