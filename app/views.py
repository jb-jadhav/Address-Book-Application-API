from urllib import response
from .models import Mybook
from .serializers import MybookSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AddressBook(APIView):
    # method for retrive records using py id
    def get(self, request, pk=None,format=None):
        id = pk
        if id is not None:
            mybook = Mybook.objects.get(id=id)
            serializer = MybookSerializers(mybook)
            return Response(serializer.data)
        mybook = Mybook.objects.all()
        serializer = MybookSerializers(mybook, many=True)
        return Response(serializer.data)
        
    # adding a data in database
    def post(self,request,format = None):
        serializer = MybookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # method for update the  records
    def put(self, request, pk, format=None):
        id=pk
        mybook = Mybook.objects.get(pk=id)
        serializer = MybookSerializers(mybook,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # method for Delete the records
    def delete(self, request, pk, format=None):
        id= pk
        mybook = Mybook.objects.get(pk=id)
        mybook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
