from django.db import models
import uuid
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    modified_at    = models.DateTimeField(auto_now=True)

class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    website = models.URLField(verbose_name='Website', blank=True, null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    modified_at    = models.DateTimeField(auto_now=True)

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    created_at     = models.DateTimeField(auto_now_add=True)
    modified_at    = models.DateTimeField(auto_now=True)

class Book(models.Model):
    COVER_TYPES = (
        ('HARD', 'Hard'),
        ('SOFT', 'Soft')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(max_length=15)
    isbn = models.CharField(max_length=100, blank=True, null=True)
    title = models.TextField()
    publication_date = models.DateField()
    size = models.CharField(max_length=15)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)
    edition = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    available_quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10,decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,  related_name='authors')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='publisher')
    genre = models.ManyToManyField(Genre, related_name='genres')
    created_at     = models.DateTimeField(auto_now_add=True)
    modified_at    = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    CUSTOMER_STATUS = (
        ('VRFY', 'Verify'),
        ('ACTV', 'Activated'),
        ('DEAC', 'Deactivated')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    email = models.EmailField()
    passwordhash = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    street_address = models.CharField(max_length=255)
    ward = models.CharField(max_length=15)
    district = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    status = models.CharField(max_length=4, choices=CUSTOMER_STATUS)
    created_at     = models.DateTimeField(auto_now_add=True)
    modified_at    = models.DateTimeField(auto_now=True)

class Discount(models.Model):
    DISCOUNT_TYPES = (
        ('PRCT', 'Percent'),
        ('CART', 'Cart'),
        ('BULK', 'Bulk'),
        ('PROD', 'Product'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=4, choices=DISCOUNT_TYPES)
    created_at     = models.DateTimeField(auto_now_add=True)
    modified_at    = models.DateTimeField(auto_now=True)

class Shipper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

class Order(models.Model):
    ORDER_STATUS = (
        (1, 'Ordered'),
        (2, 'Received'),
        (3, 'Packaging'),
        (4, 'Shipping'),
        (5, 'Done'),
        (6, 'Cancelled'),
        (7, 'Refunded'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_time =  models.DateTimeField(default=now, editable=False)
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, related_name='discount', null=True, on_delete=models.SET_NULL)
    shipper = models.ForeignKey(Shipper, related_name='shipper', null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=2, choices=ORDER_STATUS)
    created_at     = models.DateTimeField(auto_now_add=True)
    modified_at    = models.DateTimeField(auto_now=True)

class OrderDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, related_name='book', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, related_name='review_book', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='review_customer', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    modified_at    = models.DateTimeField(auto_now=True)