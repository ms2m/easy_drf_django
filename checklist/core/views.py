from django.http import Http404

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from core.models import CheckList, CheckListItem
from core.serializers import CheckListSeralizer, CheckListItemSeralizer

## Create your views here.
## create fn base view or class based views.
## serialization: converts python data types to Json
## deserialization: converts Json to python data

class TestAPIView(APIView):
    def get(self, request, format=None):
        return Response({'name': 'msingh class based view.'})

class CheckListsAPIView(APIView):
    seriailizer_class = CheckListSeralizer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = CheckList.objects.all()
        serializer = self.seriailizer_class(data, many=True)
        serilalized_data = serializer.data
        
        return Response(serilalized_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        # Code for creation
        serializer = self.seriailizer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListAPIView(APIView):
    seriailizer_class = CheckListSeralizer

    def get_obj(self, pk):
        try:
            return CheckList.objects.get(pk=pk)
        except Exception as e:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.seriailizer_class(self.get_obj(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        checklist = self.get_obj(pk)
        serializer = self.seriailizer_class(checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        checklist = self.get_obj(pk)
        checklist.delete()
        # serializer = self.seriailizer_class()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckListItemCreateAPIView(APIView):
    seriailizer_class = CheckListItemSeralizer

    # Code for creation
    def post(self, request, format=None):
        serializer = self.seriailizer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListItemAPIView(APIView):
    seriailizer_class = CheckListItemSeralizer

    def get_obj(self, pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except Exception as e:
            raise Http404

    def get(self, request, pk, format=None):
        checklist_item = self.get_obj(pk)
        serializer = self.seriailizer_class(checklist_item)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        checklist_item = self.get_obj(pk)
        serializer = self.seriailizer_class(checklist_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        checklist_item = self.get_obj(pk)
        checklist_item.delete()
        # serializer = self.seriailizer_class()
        return Response(status=status.HTTP_204_NO_CONTENT) 

