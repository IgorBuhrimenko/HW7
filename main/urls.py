
from django.urls import path


from . import views
from .views import StudentCreateView, LecturerCreateView, StudentEditView, LecturerEditView, StudentDeleteView, LecturerDeleteView


urlpatterns = (
    path('', views.index, name='index'),
    path('student', views.show_student, name='student'),
    path('lector', views.show_lector, name='lector'),
    path('group', views.show_group, name='group'),
    path('student/<int:student_id>', views.shows_students, name='show_student'),
    path('student/<int:pk>/edit', views.StudentEditView.as_view(), name='edit_student'),
    path('student/new', StudentCreateView.as_view(), name='create_student1'),
    path('lector/new', LecturerCreateView.as_view(), name='create_lecturer'),
    path('student/<int:pk>/delete', views.StudentDeleteView.as_view(), name='delete_students'),
    path('lector/<int:lecturer_id>', views.shows_lectors, name='show_lector'),
    path('lector/<int:pk>/edit', views.LecturerEditView.as_view(), name='edit_lector'),
    path('lector/<int:pk>/delete', views.LecturerDeleteView.as_view(), name='delete_lector'),
    path('group/<int:group_id>', views.shows_groups, name='show_group'),
    path('group/<int:group_id>/edit', views.edit_group, name='edit_group'),
    path('group/<int:group_id>/delete', views.delete_group, name='delete_group'),
    path('create_group', views.create_group, name='create_group'),
    path('send_message', views.send_message, name='send_message'),

)


