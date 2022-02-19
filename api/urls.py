from django.urls import path
from .views import apiOverView, taskDetail, taskList

urlpatterns = [
    path("", apiOverView, name="api-overview"),
    path("task-list/", taskList, name="task-list"),
    path("task-detail/<str:pk>", taskDetail, name="task-list")
]
