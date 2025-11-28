from django.urls import path
from app_school import views
from app_school.app_views import student_views, subject_views, teacher_views, auth_views

urlpatterns = [
    path("",views.home, name="/"),
    path("find_by_id/<id>",views.find_by_id),
    path("content.html",views.content),

    # -------------- Route Student ---------------------
    path("student/index", student_views.index),
    path("student/show", student_views.show),
    path("student/create", student_views.create),
    path("student/delete/<id>", student_views.delete),
    path("student/edit/<id>", student_views.edit),
    path("student/update/<id>", student_views.update),

    #  # -------------- Route Subject ---------------------
    path("subject/index", subject_views.index),
    path("subject/show", subject_views.show),
    path("subject/create", subject_views.create),
    path("subject/delete/<id>", subject_views.delete),
    path("subject/edit/<id>", subject_views.edit),
    path("subject/update/<id>", subject_views.update),

#  # -------------- Route Teacher ---------------------
    path("teacher/index", teacher_views.index),
    path("teacher/show", teacher_views.show),
    path("teacher/create", teacher_views.create),
    path("teacher/delete/<id>", teacher_views.delete),
    path("teacher/edit/<id>", teacher_views.edit),
    path("teacher/update/<id>", teacher_views.update),

    # # -------------- Route Auth ---------------------
    path("login/", auth_views.auth, name="login"),
    path("logout/", auth_views.user_logout, name="logout"),

]


