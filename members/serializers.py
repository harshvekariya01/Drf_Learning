from rest_framework import serializers
from members.models import student


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = [ 'id','employee_name', 'roll','city']


