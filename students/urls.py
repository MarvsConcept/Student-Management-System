from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('record/<int:pk>', views.student_record, name='record'),
    path('add_student/', views.add_student, name='add_student'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
]