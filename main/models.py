from django.db import models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField('Имя студента', max_length=100)
    last_name = models.CharField('Фамилия студента', max_length=100)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.last_name


class Lecturer(models.Model):
    lecturer_id = models.AutoField(primary_key=True)
    first_name = models.CharField('Имя лектора', max_length=100)
    last_name = models.CharField('Фамилия лектора', max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.last_name


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course = models.CharField('Название предмета', max_length=100)
    students = models.ManyToManyField(Student)
    teacher = models.OneToOneField(Lecturer, on_delete=models.CASCADE)


class Message(models.Model):
    name = models.CharField('Имя отправителя', max_length=200)
    email = models.EmailField(max_length=100)
    text_message = models.CharField('Текст меседжа', max_length=200)

    def __str__(self):
        return self.text_message

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'text': self.text_message
        }


# Create your models here.
