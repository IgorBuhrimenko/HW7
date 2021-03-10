from django.contrib import admin
from .models import Student
from .models import Lecturer
from .models import Group
from .models import Message

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Group)
admin.site.register(Message)
# Register your models here.
