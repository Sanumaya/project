from django.urls import path
from . import views

urlpatterns = [
     path('users/dashboard/', views.user_dashboard, name="user.dashboard"),
    path('users/register/', views.user_register, name="user.register"),
    path('users/login/', views.user_login, name="user.login"),
    path('users/edit/<int:user_id>', views.user_edit, name="user.edit"),
    path('users/profile/<int:user_id>', views.user_profile, name="user.profile"),
]