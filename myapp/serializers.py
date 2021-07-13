from rest_framework import serializers, status
from myapp.models import Book, Borrow
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password"
        )
        extra_kwargs = {'password': {'write_only': True}}

    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    
    def update(self, instance, validated_data):
        if "password" in validated_data:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email"
        )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "author",
            "count",
        )


class WriteBorrowSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    book = serializers.SlugRelatedField(slug_field="name", queryset=Book.objects.all())
    class Meta:
        model = Borrow
        fields = (
            "book",
            "user",
            "quantity",
            "date",
        )
    
    def create(self, validated_data):
        if "quantity" in validated_data:
            try:
                print(validated_data['book'].count)
                quantity = validated_data['quantity']
                validated_data['book'].count -=  quantity
                validated_data['book'].save()
            except:
                return Response({"Fail": "Out of stock"}, status=status.HTTP_204_NO_CONTENT)
        else:
            try:
                validated_data['book'].count -=  1
                validated_data['book'].save()
            except:
                return Response({"Fail": "Out of stock"}, status=status.HTTP_204_NO_CONTENT)  
        return super().create(validated_data)
    

class ReadBorrowSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer() 
    class Meta:
        model = Borrow
        fields = (
            "id",
            "book",
            "user",
            "quantity",
            "date",
        )