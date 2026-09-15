from rest_framework import serializers
from .models import Mixin

class MixinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mixin
        fields = "__all__"
        