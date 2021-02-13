
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student', views.show_student, name='student'),
    path('lector', views.show_lector, name='lector'),
    path('group', views.show_group, name='group'),
    path('create_student', views.create_students, name='create_student'),
    path('create_lector', views.create_lector, name='create_lector'),
    path('create_group', views.create_group, name='create_group')
]


