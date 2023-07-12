from .form import *
from .serializers import *
from .models import School, Student
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
# Create your views here.



def school_list(request):
    school = School.objects.all()
    return render(request, "school_list.html", {"schools": school})


def createstudent(request):
    form = Studentform()
    # breakpoint()
    if request.method == 'POST':
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'student_create.html', {'form':form})

def createschool(request):
    form = Schoolform()
    # breakpoint()
    if request.method == 'POST':
        form = Schoolform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school-details')
    return render(request, 'school_create.html', {'form':form})
    
def update_school(request, id):
    school_obj = School.objects.get(id=id)
    form = Schoolform(instance=school_obj)
    if request.method == 'POST':
        form = Schoolform(request.POST, instance=school_obj)
        if form.is_valid():
            form.save()
            return redirect('school-details')
    return render(request, 'school_create.html', {'form':form})

def update_student(request, id):
    student_obj = Student.objects.get(id=id)
    form = Studentform(instance=student_obj)
    if request.method == 'POST':
        form = Studentform(request.POST, instance=student_obj)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'school_create.html', {'form':form})


def student_list(request):
    students = Student.objects.all()
    return render(request, "students_list.html", {"students": students})

def delete_school(request, id):
    school_obj = School.objects.get(id=id)
    school_obj.delete()
    return redirect('school-details')


def delete_student(request, id):
    student_obj = Student.objects.get(id=id)
    student_obj.delete()
    return redirect('student_list')


@api_view(["GET"])
def school_api_detail(request, id):
    school = School.objects.get(id=id)
    serializer = SchoolSerializer(school)
    return Response(serializer.data)


@api_view(["GET"])
def student_api_detail(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)