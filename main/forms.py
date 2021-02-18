from django import forms

from .models import Student, Lecturer, Group


class addstudent(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email',)


class addlector(forms.ModelForm):

    class Meta:
        model = Lecturer
        fields = ('first_name', 'last_name', 'email',)


class addgroup(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('course', 'students', 'teacher',)


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email',)


class LectorForm(forms.ModelForm):

    class Meta:
        model = Lecturer
        fields = ('first_name', 'last_name', 'email',)


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('course', 'students', 'teacher',)



