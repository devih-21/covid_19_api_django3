from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import csv

# import unicode
# Create your views here.


class GetDataCovid19ByLocation(APIView):

    def get(self, request):
        data = requests.get("https://vnexpress.net/microservice/sheet/type/covid19_2021_by_location").content.decode('utf-8')
        result = csv.reader(data.splitlines(), delimiter=',')
        return Response(data=result, status=status.HTTP_200_OK)
