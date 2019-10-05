from .models import Author, Publisher, Genre, Book, Customer, Discount, Shipper, Order, OrderDetails, Review
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name',
                  'description', 'created_at', 'modified_at')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'website', 'created_at', 'modified_at')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'created_at', 'modified_at')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'sku', 'isbn', 'title', 'publication_date', 'size', 'cover_type', 'edition', 'available_quantity', 'price', 'author', 'publisher', 'genre', 'created_at', 'modified_at')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'passwordhash', 'phone_number', 'street_address', 'ward', 'district', 'city', 'status', 'created_at', 'modified_at')


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('id', 'name', 'value', 'type', 'created_at', 'modified_at')

class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = ('id', 'name', 'phone_number')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'date_time', 'customer', 'discount', 'shipper', 'status', 'created_at', 'modified_at')

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ('id', 'book', 'order', 'amount')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'book', 'customer', 'rating', 'comment', 'created_at', 'modified_at')