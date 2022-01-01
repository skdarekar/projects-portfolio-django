from django.urls import path
from .views import (project_home_view, project_list_view, project_add_view)

urlpatterns = [
    path('', project_home_view, name="project-home-view"),
    path('list/', project_list_view, name="project-list-view"),
    path('add/', project_add_view, name="project-add-view"),
]