from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'weather'
router = DefaultRouter()
# must add view
#router.register('weather/', views.WeatherAPIView, basename='weather')
urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.WeatherListView.as_view(), name='list'),
    path('list/<int:id>', views.WeatherDetailGenericAPIView.as_view(), name='detail'),
]
urlpatterns1 = format_suffix_patterns(urlpatterns)