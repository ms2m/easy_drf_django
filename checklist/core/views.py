from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import CheckList
from core.serializers import CheckListSeralizer

## Create your views here.
## create fn base view or class based views.
## serialization: converts python data types to Json
## deserialization: converts Json to python data

class TestAPIView(APIView):
    def get(self, request, format=None):
        return Response({'name': 'msingh class based view.'})

class CheckListsAPIView(APIView):
    seriailizer_class = CheckListSeralizer

    def get(self, request, format=None):
        data = CheckList.objects.all()
        serializer = self.seriailizer_class(data, many=True)
        serilalized_data = serializer.data
        
        return Response(serilalized_data)

