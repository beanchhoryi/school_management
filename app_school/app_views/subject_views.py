from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from unicodedata import category

from app_school.models import Subject

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from unicodedata import category

from app_school.models import Subject

@login_required(login_url='/login')
def index(request):
    if request.method == "POST":
        # FIX: Use subject_name instead of first_name
        search_item = request.POST['search_item']
        subjects = Subject.objects.filter(subject_name__contains=search_item)
        count_item = subjects.count()
        paginator = Paginator(subjects, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # REVERTED to your original variable name "subject"
        data = {"subject":page_obj,"count_item":count_item,"title": "Subject List"}
    else:
        subjects = Subject.objects.all().order_by('id')
        count_item = subjects.count()
        paginator = Paginator(subjects, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # REVERTED to your original variable name "subject"
        data = {"subject":page_obj,"count_item":count_item,"title": "Subject List"}

    return render(request, "pages/subject/index.html", context=data)

@login_required(login_url='/login')
def show(request):
    data = {"title": "Subject List"}
    return render(request, "pages/subject/create.html", context=data)

@login_required(login_url='/login')
def create(request):
    try:
        if request.method == 'POST':
            Subject.objects.create(
                subject_name=request.POST.get('subject_name'),
            )
            messages.success(request, 'Subject added successfully!')
            return redirect('/subject/index')
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
    return render(request, "pages/subject/create.html")

@login_required(login_url='/login')
def delete(request, id):
    data = {"title": "Subject List"}
    subject = Subject.objects.get(pk=id)
    subject.delete()
    messages.success(request, 'Subject deleted successfully!')
    return redirect('/subject/index')

def edit(request, id):
    subject = Subject.objects.get(pk=id)
    data = {"subject": subject, "title": "Update Subject"}
    return render(request, "pages/subject/update.html", context=data)

@login_required(login_url='/login')
def update(request, id):
    if request.method == 'POST':
        subject_exist = Subject.objects.get(pk=id)
        subject_exist.subject_name = request.POST['subject_name']
        subject_exist.full_clean()
        subject_exist.save()
        messages.success(request, 'Subject updated successfully!')
        return redirect('/subject/index')
    else:
        return redirect(f'/subject/edit/{id}')