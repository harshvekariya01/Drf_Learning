from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import  studentSerializer,ProfessionSerializer
from .models import Profession, student

class studentviewset(viewsets.ModelViewSet):
    serializer_class = studentSerializer
    queryset = student.objects.all()
    serializer = studentSerializer(queryset)


class Professionviewset(viewsets.ModelViewSet):
    serializer_class = ProfessionSerializer
    def get_queryset(self):
        queryset = Profession.objects.all()
        return queryset
    
    def list(self, request, *args, **kwargs):
        lists = Profession.objects.filter(id=6)
        serializer = ProfessionSerializer(lists,many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        return HttpResponseNotAllowed('not allowed')
    
    def create(self, request, *args, **kwargs):
        data = request.data
        creates = Profession.objects.create(name=data['name'])
        creates.save()

        serializer = ProfessionSerializer(creates)
        return Response(serializer.data)




        



