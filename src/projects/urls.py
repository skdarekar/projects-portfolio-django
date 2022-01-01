from django.urls import path
from .views import (project_home_view, 
project_list_view, 
project_add_view, 
project_detail_view,
project_edit_view)

urlpatterns = [
    path('', project_home_view, name="project-home-view"),
    path('list/', project_list_view, name="project-list-view"),
    path('<int:project_id>', project_detail_view, name="project-detail-view"),
    path('<int:project_id>/update', project_edit_view, name="project-update-view"),
    path('add/', project_add_view, name="project-add-view"),
]