from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField("get_abs_url")

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["user", "id"]

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def create(self, validated_data):
        validated_data["user"] = self.context.get("request").user
        return super().create(validated_data)
