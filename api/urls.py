from django.urls import path
from .views import apiOverView, taskDelete, taskDetail, taskList, taskCreate, taskUpdate, HomeView

urlpatterns = [
    path("", HomeView, name="home"),
    path("api/", apiOverView, name="api-overview"),
    path("api/task-list/", taskList, name="task-list"),
    path("api/task-detail/<str:pk>", taskDetail, name="task-list"),
    path('api/task-create/', taskCreate, name="task-create"),
    path("api/task-update/<str:pk>", taskUpdate, name="task-update"),
    path("api/task-delete/<str:pk>", taskDelete, name="task-delete")
]
