from rest_framework import serializers
from weather.models import City

class WeatherSerializers(serializers.ModelSerializer):
    #city = serializers.CharField(max_length=50)
    snippet = serializers.ReadOnlyField(source="get_snippet")
    absolute_url = serializers.SerializerMethodField(
        method_name="get_abs_url"
    )

    class Meta:
        model = City
        fields = '__all__'

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)
