from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects_list, name='projects_list'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/new', views.add_project, name='add_project'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
]


# path('projects/', views.projects_list, name='projects_list') handles the /projects URL and maps it to the projects_list view.