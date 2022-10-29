from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('create/', views.CreateTask.as_view(), name='create_task'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update-task'),
    path('complete/<int:pk>', views.CompleteTask.as_view(), name='complete-task'),
    path('delete/<int:pk>', views.DeleteTask.as_view(), name='delete-task'),
    path('api/v1/', include('todo.api.v1.urls'))
]
