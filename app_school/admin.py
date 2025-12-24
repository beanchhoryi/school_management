from django.contrib import admin

from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import Subject

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'dob', 'address']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'dob', 'address', 'salary']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name']

