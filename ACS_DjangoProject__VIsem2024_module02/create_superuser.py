import os
import django
from django.contrib.auth.models import User

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ACS_DjangoProject__VIsem2024_module02.settings')

try:
    django.setup()
except Exception as e:
    print(f"Error setting up Django: {e}")
    raise

# Create the superuser
username = 'maroli'
email = 'rohan@gmail.com'
password = '123'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully.")
else:
    print(f"Superuser '{username}' already exists.")
