from rest_framework.viewsets import ModelViewSet
from .serializers import  studentSerializer
from .models import student
class studentviewset(ModelViewSet):
    serializer_class = studentSerializer
    queryset = student.objects.all()
    serializer = studentSerializer(queryset)


