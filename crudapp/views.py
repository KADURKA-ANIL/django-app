from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from django.http import JsonResponse
import json
# Create your views here.

@csrf_exempt
def get_students(request):
    Students = Student.objects.all()
    print(Students)
    print("return type")
    x = Students.values()
    print(x)
    print("xyz")
    y = list(x)
    print(y)
    print("chandra mukhi")
    return JsonResponse(y,safe=False)


@csrf_exempt
def get_student(request,name):
    student = Student.objects.get(name=name)
    return JsonResponse({
        "name":student.name,
        "age":student.age,
        "email":student.email
    })


@csrf_exempt
def update_student(request):
    
    if request.method == "PUT":
        print(request.body)
        data = json.loads(request.body)
        print(data)
        new_age = data['new_age']
        old_age = data['old_age']
        student = Student.objects.get(age=old_age)
        student.age = new_age
        student.save()
        return JsonResponse({
           "Message": f"{old_age} updated successfully to {new_age}"
        })


@csrf_exempt
def create_student(request):
    
    if request.method == "POST":
        print(request.body)
        data = json.loads(request.body)
        print(data)
        student = Student.objects.create(name=data['name'],age=data['age'],scholarship=data['scholarship'],email=data['email'])
        student.save()
        return JsonResponse({
           "Message": f"{data['name']} stored successfully in our database"
        })




@csrf_exempt
def delete_student(request,name):
    if request.method == "DELETE":
        student = Student.objects.get(name=name)
        student.delete()
        return JsonResponse({
        "Message":f"data with {name} deleted succesfully"
        })






