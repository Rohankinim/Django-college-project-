from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from .models import Student, Project
from .forms import ContactForm, ProjectForm
import csv
from reportlab.pdfgen import canvas  # type: ignore

# Home Page
def home(request):
    return render(request, 'home.html')

# Contact Form
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., send an email, save to the database, etc.)
            return HttpResponse('Thank you for your message.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Add Project
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Replace 'project_list' with your actual project list view name
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

# Project List
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

# Student List View
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

# Student Detail View
class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'

# Export Students as CSV
def export_students_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Age', 'Course'])
    students = Student.objects.all().values_list('name', 'age', 'course')
    for student in students:
        writer.writerow(student)
    return response

# Export Students as PDF
def export_students_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'
    p = canvas.Canvas(response)
    students = Student.objects.all()
    y = 800
    for student in students:
        p.drawString(100, y, f'Name: {student.name}, Age: {student.age}, Course: {student.course}')
        y -= 20
    p.showPage()
    p.save()
    return response

# AJAX Search Functionality
def search_student(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(name__icontains=query)
    results = [{'id': student.id, 'name': student.name} for student in students]
    return JsonResponse({'results': results})

def get_student_courses(request):
    student_id = request.GET.get('student_id')
    try:
        student = Student.objects.get(pk=student_id)
        courses = student.course_set.all()
        results = [{'id': course.id, 'name': course.name} for course in courses]
    except Student.DoesNotExist:
        results = []
    return JsonResponse({'courses': results})

# Student Search View
def student_search_view(request):
    return render(request, 'student_search.html')

from django.http import JsonResponse
from .models import Student

def search_student(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(name__icontains=query) if query else Student.objects.none()
    results = [{'id': student.id, 'name': student.name} for student in students]
    return JsonResponse({'results': results})
