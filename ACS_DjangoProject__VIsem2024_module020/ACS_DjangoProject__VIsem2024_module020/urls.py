from django.contrib import admin
from django.urls import path, include
from myapp.views import home, export_students_csv, export_students_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', home, name='home'),  # Root URL pattern
    path('export/csv/', export_students_csv, name='export_students_csv'),
    path('export/pdf/', export_students_pdf, name='export_students_pdf'),
]


