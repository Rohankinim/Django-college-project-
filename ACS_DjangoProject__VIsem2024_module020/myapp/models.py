from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, default='Default Course Name')
    description = models.TextField()

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)  # assuming a Course with ID 1 exists

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name

class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    languages_used = models.CharField(max_length=200)
    duration = models.DurationField()

    def __str__(self):
        return self.topic
