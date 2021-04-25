from django.test import TestCase
from django.conf import settings
from django.urls import reverse
import pytest


from main.models import Student, Lecturer, Group


class StudentViewTest(TestCase):

    NUMBER_STUDENTS = 10

    @classmethod
    def setUpTestData(cls):
        cls.firs_name = 'Ivan'
        cls.last_name = 'Ivanov'
        cls.email = 'iva@css.com'
        for stud_num in range(cls.NUMBER_STUDENTS):
            Student.objects.create(
                first_name=cls.firs_name,
                last_name=cls.last_name,
                email=cls.email
            )

    def test_view_student_url_exists_at_desired_location(self):
        resp = self.client.get('/student')
        self.assertEqual(resp.status_code, 200)

    def test_view_student_url_accessible_by_name(self):
        resp = self.client.get(reverse('student'))
        self.assertEqual(resp.status_code, 200)

    def test_lists_all_students(self):
        resp = self.client.get(reverse('student'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['students']) == self.NUMBER_STUDENTS)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('student'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main/students.html')


class LecturerViewTest(TestCase):

    NUMBER_LECTURER = 10

    @classmethod
    def setUpTestData(cls):
        cls.firs_name = 'Ivan'
        cls.last_name = 'Ivanov'
        cls.email = 'iva@css.com'
        for lector_num in range(cls.NUMBER_LECTURER):
            Lecturer.objects.create(
                first_name=cls.firs_name,
                last_name=cls.last_name,
                email=cls.email
            )

    def test_view_lecturers_url_exists_at_desired_location(self):
        resp = self.client.get('/lector')
        self.assertEqual(resp.status_code, 200)

    def test_view_lecturers_url_accessible_by_name(self):
        resp = self.client.get(reverse('lector'))
        self.assertEqual(resp.status_code, 200)

    def test_lists_all_lecturers(self):
        resp = self.client.get(reverse('lector'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['lecturers']) == self.NUMBER_LECTURER)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('lector'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main/lector.html')


class GroupListViewTest(TestCase):
    NUMBER_STUDENT = 10
    NUMBER_GROUP = 10

    @classmethod
    def setUpTestData(cls):
        cls.first_name = "Ivan"
        cls.last_name = "Ivanov"
        cls.email = "Ivava@sss.com"
        cls.course = 'Astronomy'
        for pr in range(cls.NUMBER_GROUP):
                teacher = Lecturer.objects.create(
                    first_name=f'first name{pr}',
                    last_name=f'last name{pr}',
                    email=f'{pr}br@br.com',
                )
                group = Group.objects.create(course=cls.course ,teacher=teacher)
        for num in range(cls.NUMBER_STUDENT):
            student = Student.objects.create(first_name=cls.first_name,
                                             last_name=cls.last_name,
                                             email=cls.email,
                                                )
            group.students.add(student)

    def test_view_groups_url_exists_at_desired_location(self):
        resp = self.client.get('/group')
        self.assertEqual(resp.status_code, 200)

    def test_view_groups_url_accessible_by_name(self):
        resp = self.client.get(reverse('group'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('group'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'main/group.html')


