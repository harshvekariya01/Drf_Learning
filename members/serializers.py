from rest_framework import serializers
from .models import Profession, student


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('id','employee_name', 'roll','city')


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ('id','name','active')

