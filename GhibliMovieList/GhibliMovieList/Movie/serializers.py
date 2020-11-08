from rest_framework import serializers
from .models import Movie
from MovieCharacter.models import People
from MovieCharacter.serializers import CreatePeopleSerializers


class CreateMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','description','director','producer','release_date','rt_score')

class ListMovieSerializer(serializers.ModelSerializer):
    character = CreatePeopleSerializers(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


