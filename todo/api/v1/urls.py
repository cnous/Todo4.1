from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

app_name = 'api-v1'
router = DefaultRouter()
router.register('task', views.TaskModelViewSet, basename='task-list')


urlpatterns = router.urls