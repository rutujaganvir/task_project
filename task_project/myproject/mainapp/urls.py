from . import views
from django.urls import path

urlpatterns = [
    path('create/', views.createstudent, name="create" ),
    path('student_list/', views.student_list, name="student_list" ),
    path('school-details/', views.school_list, name='school-details'),
    path('create-school/', views.createschool, name="school" ),
    path('update_school/<int:id>/', views.update_school, name="update-school" ),
    path('update_student/<int:id>/', views.update_student, name="update-student" ),
    path('delete_school/<int:id>/', views.delete_school, name="delete-school" ),
    path('delete_student/<int:id>/', views.delete_student, name="delete-student" ),
    path('get/school/<int:id>/', views.school_api_detail, name="get-school" ),
    path('get/student/<int:id>/', views.student_api_detail, name="get-student" )


]