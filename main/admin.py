from django.contrib import admin
from django.http import HttpResponse

import csv

from .models import Student
from .models import Lecturer
from .models import Group
from .models import Message


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'course', 'teacher')
    filter_horizontal = ('students',)
    actions = ['export']

    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="groups.csv"'
        writer = csv.writer(response)
        header = ['Course', 'Teacher', 'Students']
        writer.writerow(header)
        for group in queryset:
            lector_name = f'{group.teacher.first_name} {group.teacher.last_name}'
            students = []
            for student in group.students.all():
                student_name = f'{student.first_name} {student.last_name}'
                students.append(student_name)
            row = [group.course,
                   lector_name,
                   students
                   ]
            writer.writerow(row)
        return response

    export.short_description = 'Export group'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    actions = ['export']

    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students.csv"'
        writer = csv.writer(response)
        header = ['full_name', 'email']
        writer.writerow(header)
        for student in queryset:
            full_name = f'{student.first_name} {student.last_name}'
            row = [full_name,
                   student.email
                   ]
            writer.writerow(row)
        return response

    export.short_description = 'Export students'


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    actions = ['export']

    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lector.csv"'
        writer = csv.writer(response)
        header = ['lector', 'email']
        writer.writerow(header)
        for lector in queryset:
            lector_name = f'{lector.first_name} {lector.last_name}'

            row = [
                lector_name,
                lector.email
            ]
            writer.writerow(row)
        return response

    export.short_description = 'Export lectors'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'text_message')

# Register your models here.
