from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from unicodedata import category

from app_school.models import Student

@login_required(login_url='/login')
def index(request):
    if request.method == "POST":
        search_item = request.POST['search_item']  # Simplified
        students = Student.objects.filter(first_name__contains=search_item)
        count_item = students.count()
        paginator = Paginator(students, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {
            "students": page_obj,
            "count_item": count_item,
            "title": "Student List",
            "search_action": "/student/index",
            "current_model": "student"
        }
    else:
        students = Student.objects.all().order_by('id')
        count_item = students.count()
        paginator = Paginator(students, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {
            "students": page_obj,
            "count_item": count_item,
            "title": "Student List",
            "search_action": "/student/index",
            "current_model": "student"
        }

    return render(request, "pages/student/index.html", context=data)

def show(request):
    data = {"title": "Student List"}
    return render(request, "pages/student/create.html", context=data)

@login_required(login_url='/login')
def create(request):
    try:
        if request.method == 'POST':
            Student.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                gender=request.POST.get('gender'),
                dob=request.POST.get('dob'),
                address=request.POST.get('address')
            )
            messages.success(request, 'Student added successfully!')
            return redirect('/student/index')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
    return render(request, "pages/student/create.html")

@login_required(login_url='/login')
def delete(request, id):
    data = {"title": "Student List"}
    student = Student.objects.get(pk=id)
    student.delete()
    messages.success(request, 'Student deleted successfully!')
    return redirect('/student/index')

def edit(request, id):
    student = Student.objects.get(pk=id)
    data = {"student":student, "title": "Update Student"}
    return render(request, "pages/student/update.html", context=data)

@login_required(login_url='/login')
def update(request, id):
    if request.method == 'POST':  # ← ADD THIS CHECK
        student_exist = Student.objects.get(pk=id)
        student_exist.first_name = request.POST['first_name']
        student_exist.last_name = request.POST['last_name']
        student_exist.gender = request.POST['gender']
        student_exist.dob = request.POST['dob']
        student_exist.address = request.POST['address']
        student_exist.full_clean()
        student_exist.save()
        messages.success(request, 'Student updated successfully!')
        return redirect('/student/index')
    else:
        # Handle GET request - redirect back to edit page
        return redirect(f'/student/edit/{id}')
