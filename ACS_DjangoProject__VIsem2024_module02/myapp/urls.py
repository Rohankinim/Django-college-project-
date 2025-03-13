from django.urls import path
from .views import item_create, item_success

urlpatterns = [
    path('create/', item_create, name='item_create'),
    path('success/', item_success, name='item_success'),
]
