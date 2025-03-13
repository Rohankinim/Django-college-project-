# myapp/urls.py

from django.urls import path
from .views import (
    add_project,
    StudentListView,
    StudentDetailView,
    export_students_csv,
    export_students_pdf,
    search_student,
    get_student_courses,
    student_search_view,
    contact,
    project_list,
    home
)
from django.urls import path
from .views import search_student

urlpatterns = [
    # Home page
    path('', home, name='home'),

    # Contact page
    path('contact/', contact, name='contact'),

    # Project-related URLs
    path('add_project/', add_project, name='add_project'),
    path('projects/', project_list, name='project_list'),

    # Student-related URLs
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),

    # Export URLs
    path('export/csv/', export_students_csv, name='export_students_csv'),
    path('export/pdf/', export_students_pdf, name='export_students_pdf'),

    # AJAX search and courses URLs
    path('search_student/', search_student, name='search_student'),
    path('get_student_courses/', get_student_courses, name='get_student_courses'),

    # Student search page
    path('student_search/', student_search_view, name='student_search'),

   
]

