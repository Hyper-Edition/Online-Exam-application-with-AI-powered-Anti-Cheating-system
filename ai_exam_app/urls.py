from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('base/', views.base, name='base'),
    path('cheating_report/', views.cheating_report, name='cheating_report'),
    path('contact/', views.contact, name='contact'),
    path('exam_list/', views.exam_list, name='exam_list'),
    path('exam/', views.exam, name='exam'),
    path('student_login/', views.stud_login, name='student_login'),
    path('teacher_login/', views.teach_login, name='teacher_login'),
    path('monitor/', views.monitor, name='monitor'),
    path('result/', views.result, name='result'),
    path('signup/', views.signup, name='signup'),
    path('teacher_profile/', views.teacher_profile, name='teacher_profile'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student_registration/', views.stud_reg, name='student_registration'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher_registration/', views.teach_reg, name='teacher_registration'),
    
]
