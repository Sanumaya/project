from django.urls import path,include
from . import views
from .views import StudentDetailApiView
from new_app.models import StudentDetail 

urlpatterns = [
    path('users/dashboard/', views.user_dashboard, name="user.dashboard"),
    path('users/register/', views.user_register, name="user.register"),
    path('users/login/', views.user_login, name="user.login"),
    path('users/edit/<int:user_id>', views.user_edit, name="user.edit"),
    path('users/profile/<int:user_id>', views.user_profile, name="user.profile"),
    path('users/logout/', views.user_logout, name="user.logout"),

#api_url
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/students/', StudentDetailApiView.as_view()),
]