# Generated by Django 3.1.7 on 2021-03-21 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_student_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cover',
            field=models.ImageField(default='covers/student_photo/default.png', upload_to='covers/student_photo'),
        ),
    ]
