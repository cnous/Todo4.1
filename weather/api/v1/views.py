from rest_framework.response import Response
import requests
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveDestroyAPIView
from .serializers import WeatherSerializers
from weather.models import City
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class WeatherListView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = WeatherSerializers

class WeatherDetailGenericAPIView(RetrieveDestroyAPIView):
    serializer_class = WeatherSerializers
    queryset = City.objects.all()
    lookup_field = 'id'

    @method_decorator(cache_page(60 * 20))
    def get(self, request, id):
        city = str(City.objects.filter(pk=id)[0])
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7e36b590338e65f32f825b98b80bbf60'
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types
        return Response(city_weather)

