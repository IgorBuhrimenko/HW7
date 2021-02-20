from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Student, Lecturer


@receiver(pre_save, sender=Student)
def capitalize_student(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()


@receiver(pre_save, sender=Lecturer)
def capitalize_lecturer(sender, instance, **kwargs):
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()
