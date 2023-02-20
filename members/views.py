from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import  studentSerializer,ProfessionSerializer
from .models import Profession, student



class Professionviewset(viewsets.ModelViewSet):
    serializer_class = ProfessionSerializer
    queryset =  Profession.objects.all()
    lookup_field = 'id'

    # def list(self, request, *args, **kwargs):
    #     lists = Profession.objects.all()
    #     serializer = ProfessionSerializer(lists,many=True)
    #     return Response(serializer.data)    

    # def retrieve(self, request, *args, **kwargs):
    #     id = kwargs['id']
    #     queryset = Profession.objects.get(id=self.kwargs['id'])
    #     queryset = self.get_object()
    #     serializer = ProfessionSerializer(queryset)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     creates = Profession.objects.create(name=data['name'])
    #     creates.save()
    #     serializer = ProfessionSerializer(creates)
    #     return Response(serializer.data)


class studentviewset(viewsets.ModelViewSet):
    serializer_class = studentSerializer
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        lists = student.objects.all()
        serializer = self.serializer_class(lists,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        id = kwargs['id']
        queryset = student.objects.get(id=self.kwargs['id'])
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        creates = student.objects.create(employee_name=data['employee_name'],roll=data['roll'],city=data['city'])
        creates.save()
        serializer = studentSerializer(creates)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        id = kwargs['id']
        queryset = student.objects.get(id=self.kwargs['id'])
        serializer = self.serializer_class(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, *args, **kwargs):
        id = kwargs['id']
        queryset = student.objects.get(id=self.kwargs['id'])
        queryset.delete()
        return Response('data has been deleted')

    
    def update(self,request, *args, **kwargs):
        id = kwargs['id']
        print(request.data['employee_name'],"===============================================")
        print(request.data['roll'],"===============================================")
        
        print(request.data['city'],"===============================================")
        queryset = student.objects.get(id=self.kwargs['id'])
        queryset.employee_name = request.data['employee_name']
        queryset.roll = request.data['roll']
        queryset.city = request.data['city']

        serializer = self.serializer_class(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




        



