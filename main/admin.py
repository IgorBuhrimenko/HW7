from django.contrib import admin
from .models import Student
from .models import Lecturer
from .models import Group

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Group)

# Register your models here.
