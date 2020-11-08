from rest_framework import serializers
from .models import People


class CreatePeopleSerializers(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = "__all__"
