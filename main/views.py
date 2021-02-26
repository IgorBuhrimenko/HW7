from django.shortcuts import get_object_or_404, render, redirect
from .models import Lecturer, Student, Group
from .forms import addstudent, addlector, addgroup, StudentForm, LectorForm, GroupForm, MessageForm


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


def show_student(request):
    students = Student.objects.all().order_by()
    return render(request, 'main/students.html', {'title': 'Студенты', 'students': students})


def shows_students(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'main/showstudent.html', {'student': student})


def show_lector(request):
    lecturers = Lecturer.objects.all().order_by()
    return render(request, 'main/lector.html', {'title': 'Преподователи', 'lecturers': lecturers})


def shows_lectors(request, lecturer_id):
    lector = get_object_or_404(Lecturer, lecturer_id=lecturer_id)
    return render(request, 'main/showlector.html', {'lector': lector})


def show_group(request):
    groups = Group.objects.all().order_by()
    return render(request, 'main/group.html', {'title': 'Курсы', 'groups': groups})


def shows_groups(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    return render(request, 'main/showgroup.html', {'group': group})


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


def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student')
    else:
        form = StudentForm(instance=student)
    return render(request, 'main/editstudent.html', {'form': form})


def delete_students(requests, student_id):
    Student.objects.filter(student_id=student_id).delete()
    return redirect('student')


def edit_lector(request, lecturer_id):
    lector = get_object_or_404(Lecturer, lecturer_id=lecturer_id)
    if request.method == 'POST':
        form = LectorForm(request.POST, instance=lector)
        if form.is_valid():
            lector = form.save(commit=False)
            lector.save()
            return redirect('lector')
    else:
        form = LectorForm(instance=lector)
    return render(request, 'main/editlector.html', {'form': form})


def delete_lector(requests,lecturer_id):
    Lecturer.objects.filter(lecturer_id=lecturer_id).delete()
    return redirect('lector')


def edit_group(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save()
            group.save()
            return redirect('group')
    else:
        form = GroupForm(instance=group)
    return render(request, 'main/editgroup.html', {'form': form})


def delete_group(request, group_id):
    Group.objects.filter(group_id=group_id).delete()
    return redirect('group')


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('send_message')
    else:
        form = MessageForm()
    return render(request, 'main/sendmessage.html', {'form': form})


