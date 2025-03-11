from django.urls import path
from  .  import views

urlpatterns = [
    path("all_students/", views.get_students, name="get_students"),
    path("student/get_student/<str:name>", views.get_student, name="get_student"),
    path("student/update_student/", views.update_student, name="update_student"),
    path("student/create_student/", views.create_student, name="create_student"),
    path("student/delete_student/<str:name>", views.delete_student, name="delete_student"),
]