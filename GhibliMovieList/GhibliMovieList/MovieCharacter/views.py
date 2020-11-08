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
from .models import Product
from .serializers import  CreatePeopleSerializers
import datetime
import pdb
from MovieCharacter.models import  People
from MovieCharacter.models import People
from rest_framework.parsers import JSONParser


class CreatePeopleViewSets(ModelViewSet):
    serializer_class = CreatePeopleSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)


