from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from unicodedata import category

from app_school.models import Teacher

@login_required(login_url='/login')
def index(request):
    if request.method == "POST":
        teacher = Teacher()
        teacher.first_name=request.POST['search_item']
        teachers = Teacher.objects.filter(first_name__contains=teacher.first_name)
        count_item = teachers.count()
        paginator = Paginator(teachers, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        data = {"teacher":page_obj,"count_item":count_item,"title": "Teacher List"}
    else:
        teachers = Teacher.objects.all().order_by('id')
        count_item = teachers.count()
        paginator = Paginator(teachers, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # REVERTED to your original variable name "teacher"
        data = {"teacher":page_obj,"count_item":count_item,"title": "Teacher List"}

    return render(request, "pages/teacher/index.html", context=data)

@login_required(login_url='/login')
def show(request):
    data={"title":"teacher List"}
    return render(request, "pages/teacher/create.html", context=data)

@login_required(login_url='/login')
def create(request):
    try:
        if request.method == 'POST':
            Teacher.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                gender=request.POST.get('gender'),
                dob=request.POST.get('dob'),
                address=request.POST.get('address'),
                salary = request.POST.get('salary')
            )
            messages.success(request, 'Teacher added successfully!')
            return redirect('/teacher/index')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
    return render(request, "pages/teacher/create.html")

@login_required(login_url='/login')
def delete(request, id):
    data = {"title": "teacher List"}
    teacher = Teacher.objects.get(pk=id)
    teacher.delete()
    messages.success(request, 'teacher deleted successfully!')
    return redirect('/teacher/index')

def edit(request, id):
    teacher = Teacher.objects.get(pk=id)
    data = {"teacher":teacher, "title": "Update teacher"}
    return render(request, "pages/teacher/update.html", context=data)

@login_required(login_url='/login')
def update(request, id):
    if request.method == 'POST':  # ← ADD THIS CHECK
        teacher_exist = Teacher.objects.get(pk=id)
        teacher_exist.first_name = request.POST['first_name']
        teacher_exist.last_name = request.POST['last_name']
        teacher_exist.gender = request.POST['gender']
        teacher_exist.dob = request.POST['dob']
        teacher_exist.address = request.POST['address']
        teacher_exist.salary = request.POST['salary']
        teacher_exist.full_clean()
        teacher_exist.save()
        messages.success(request, 'Teacher updated successfully!')
        return redirect('/teacher/index')
    else:
        # Handle GET request - redirect back to edit page
        return redirect(f'/teacher/edit/{id}')
