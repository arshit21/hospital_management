from django.urls import path
from . import views

urlpatterns = [
    path('register/staff/', views.register_staff, name='register_staff'),
    path('register/patient/', views.register_patient, name='register_patient'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('<int:user_id>/add_illness', views.add_illness, name='add_illness'),
    path('<int:user_id>/add_prescription', views.add_prescription, name='add_prescription')
    ]