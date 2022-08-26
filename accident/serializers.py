from rest_framework import serializers, viewsets
from .models import Call


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'

