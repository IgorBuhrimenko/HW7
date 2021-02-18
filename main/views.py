from django.shortcuts import render,redirect
from .models import Lecturer, Student, Group
from .forms import addstudent, addlector, addgroup


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


def show_student(request):
    students = Student.objects.all().order_by()
    return render(request, 'main/students.html', {'title': 'Студенты', 'students': students})


def show_lector(request):
    lecturers = Lecturer.objects.all().order_by()
    return render(request, 'main/lector.html', {'title': 'Преподователи', 'lecturers': lecturers})


def show_group(request):
    groups = Group.objects.all().order_by()
    return render(request, 'main/group.html', {'title': 'Курсы', 'groups': groups})


def create_students(request):
    if request.method == 'POST':
        form = addstudent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_student')
    else:
        form = addstudent()
    return render(request, 'main/getstudent.html', {'title': 'Добавить студента', 'form': form})


def create_lector(request):
    if request.method == 'POST':
        form = addlector(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_lector')
    else:
        form = addlector()
    return render(request, 'main/addlector.html', {'title': 'Добавить студента', 'form': form})


def create_group(request):
    if request.method == 'POST':
        form = addgroup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_group')
    else:
        form = addgroup()
    return render(request, 'main/addgroup.html', {'title': 'Добавить группу', 'form': form})


