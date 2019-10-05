"""ken_book_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from bookstore.views import AuthorViewSet, PublisherViewSet, GenreViewSet, BookViewSet, CustomerViewSet, DiscountViewSet, ShipperViewSet, OrderViewSet, OrderDetailsViewSet, ReviewViewSet


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'books', BookViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'shippers', ShipperViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderDetailss', OrderDetailsViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]
