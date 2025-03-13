from django.contrib import admin
from django.urls import path, include
from myapp.views import item_create  # Import the view to use

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', include('myapp.urls')),
    path('', item_create, name='home'),  # Add this line to handle the root URL
]
