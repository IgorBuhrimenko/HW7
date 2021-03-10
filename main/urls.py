
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student', views.show_student, name='student'),
    path('lector', views.show_lector, name='lector'),
    path('group', views.show_group, name='group'),
    path('student/<int:student_id>', views.shows_students, name='show_student'),
    path('student/<int:student_id>/edit', views.edit_student, name='edit_student'),
    path('student/<int:student_id>/delete', views.delete_students, name='delete_students'),
    path('lector/<int:lecturer_id>', views.shows_lectors, name='show_lector'),
    path('lector/<int:lecturer_id>/edit', views.edit_lector, name='edit_lector'),
    path('lector/<int:lecturer_id>/delete', views.delete_lector, name='delete_lector'),
    path('group/<int:group_id>', views.shows_groups, name='show_group'),
    path('group/<int:group_id>/edit', views.edit_group, name='edit_group'),
    path('group/<int:group_id>/delete', views.delete_group, name='delete_group'),
    path('create_student', views.create_students, name='create_student'),
    path('create_lector', views.create_lector, name='create_lector'),
    path('create_group', views.create_group, name='create_group'),
    path('send_message', views.send_message, name='send_message'),

]


