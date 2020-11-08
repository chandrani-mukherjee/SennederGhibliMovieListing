from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
import pandas as pd
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError
from django.conf import settings
from rest_framework import filters
from .models import Movie
from .serializers import CreateMovieSerializers, ListMovieSerializer
import datetime
import pdb
from Movie.models import  Movie
from MovieCharacter.models import People
from rest_framework.parsers import JSONParser
import requests
import json
from MovieCharacter.serializers import CreatePeopleSerializers

       
class CreateMovieViewSets(ModelViewSet):
    serializer_class = ListMovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    queryset = Movie.objects.all().order_by('release_date').reverse()


    def create(self, request, *args, **kwargs):
        
        peopleResp = requests.get('https://ghibliapi.herokuapp.com/people/')
        peopleList = peopleResp.content
        
        peopleStr = str(peopleList)
        
        peopleStr = peopleStr.replace("\\n","")
        
        peopleStr = peopleStr.strip('\'')
        peopleStr = peopleStr.strip('b\'')
        peopleList = json_array = json.loads(str(peopleStr))
        
        print(peopleList[0])

        
        for peopleItem in peopleList:
            print(peopleItem)
            peopleSerializer = CreatePeopleSerializers(data = peopleItem)
            if peopleSerializer.is_valid():
                peopleSerializer.save()
            else:
                print("Character Serializer not valid", peopleSerializer.errors)
            filmList = peopleItem["films"]
            print(filmList)
            for filmUrl in filmList:
                
                filmId = filmUrl.split('/')[-1]
                print(filmId)
                filmResp = requests.get('https://ghibliapi.herokuapp.com/films/' +  str(filmId))
                filmContent = filmResp.content
                filmJson = json.loads(filmContent)
                print(filmJson)
                movieObj = None
                try:
                    movieObj = Movie.objects.get(id=filmJson["id"])
                except Movie.DoesNotExist:
                    movieObj = None
                if movieObj:
                    pass
                else:
                    movieSerializer = CreateMovieSerializers(data = filmJson)
                
                    if movieSerializer.is_valid():
                            movieSerializer.save()
                            print("Serializer saved -- character")
                    else:
                            print("Movie Serializer not valid", movieSerializer.errors)
                            
                try:
                    movieObj = Movie.objects.get(id=filmJson["id"])
                    movieObj.character.add(peopleSerializer['id'].value)
                except Exception as e:
                    print("Exception is ", str(e))
                    movieObj = None
                
        return Response({'info': 'Movie Details created successfully'})
    
