from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView

)

from core.models import CheckList, CheckListItem
from core.permissions import IsOwner

from core.serializers import CheckListSeralizer, CheckListItemSeralizer

## Create your views here.
## create fn base view or class based views.
## serialization: converts python data types to Json
## deserialization: converts Json to python data

class CheckListsAPIView(ListCreateAPIView):
    """
    Listing, Creation
    """
    ## converting into genric view.
    serializer_class = CheckListSeralizer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset

    # def get(self, request, format=None):
    #     # data = CheckList.objects.all()
    #     ## access only which user created data.
    #     data = CheckList.objects.filter(user=request.user)
    #     serializer = self.serializer_class(data, many=True)
    #     serilalized_data = serializer.data
    #     return Response(serilalized_data, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     # context is for resolution of below error i.e. for accessing user data login
    #     #  return serializer_field.context['request'].user
    #     serializer = self.serializer_class(data=request.data, context={"request": request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrivel, Update, Destroy
    """
    ## converting into genric view.
    serializer_class = CheckListSeralizer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset


    # def get_obj(self, pk):
    #     try:
    #         obj = CheckList.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, obj)
    #         return obj
    #     except Exception as e:
    #         if 'permission' in str(e):
    #             raise e
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     serializer = self.serializer_class(self.get_obj(pk))
    #     serialized_data = serializer.data
    #     return Response(serialized_data, status=status.HTTP_200_OK)

    # def put(self, request, pk, format=None):
    #     checklist = self.get_obj(pk)
    #     serializer = self.serializer_class(checklist, data=request.data, context={"request": request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     checklist = self.get_obj(pk)
    #     checklist.delete()
    #     # serializer = self.serializer_class()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CheckListItemCreateAPIView(CreateAPIView):
    """
    Creation
    """
    serializer_class = CheckListItemSeralizer
    permission_classes = [IsAuthenticated, IsOwner]

    # # Code for creation
    # def post(self, request, format=None):
    #     serializer = self.serializer_class(data=request.data, context={"request": request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListItemAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrivel, Update, Destroy
    """
    serializer_class = CheckListItemSeralizer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckListItem.objects.filter(user=self.request.user)
        return queryset


    # def get_obj(self, pk):
    #     try:
    #         obj = CheckListItem.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, obj)
    #         return obj
    #         # return CheckListItem.objects.get(pk=pk)
    #     except Exception as e:
    #         if 'permission' in str(e):
    #             raise e
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     checklist_item = self.get_obj(pk)
    #     serializer = self.serializer_class(checklist_item)
    #     serialized_data = serializer.data
    #     return Response(serialized_data, status=status.HTTP_200_OK)

    # def put(self, request, pk, format=None):
    #     checklist_item = self.get_obj(pk)
    #     serializer = self.serializer_class(checklist_item, data=request.data, context={"request": request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     checklist_item = self.get_obj(pk)
    #     checklist_item.delete()
    #     # serializer = self.serializer_class()
    #     return Response(status=status.HTTP_204_NO_CONTENT) 

