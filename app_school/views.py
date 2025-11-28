from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from app_school.models import Student, Teacher, Subject

@login_required(login_url='/login')

def home(request):
    data={"title":"Dashboard"}
    return render(request, "index.html", context=data)

def find_by_id(request,id):
    return HttpResponse(f"id:{id}")

def content(request):
    return render(request, "pages/content.html")


