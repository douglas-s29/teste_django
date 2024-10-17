from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import TimeEntryListView
from .views import CustomLoginView

urlpatterns = [
    # Rotas de autenticação
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    # Rotas principais
    path('', views.home, name='home'),
    path('create_task/', views.create_task, name='create_task'),
    path('tasks/', views.tasks, name='tasks'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('time_entries/', views.list_time_entries, name='list_time_entries'),
    path('tasks/<int:task_id>/time_entries/create/', views.create_time_entry, name='create_time_entry'),
    path('time_entries/', TimeEntryListView.as_view(), name='list_time_entries'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('toggle_admin/<int:user_id>/', views.toggle_admin, name='toggle_admin'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]
