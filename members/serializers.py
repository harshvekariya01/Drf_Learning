from rest_framework import serializers
from .models import Profession, student


class studentSerializer(serializers.ModelSerializer):

    class Meta:
        model = student
        fields = ('id','employee_name', 'roll','city')


class ProfessionSerializer(serializers.ModelSerializer):
    # num_profession_no = serializers.SerializerMethodField() 
    # profession_no = studentSerializer(many=True)

    class Meta:
        model = Profession
        fields = ('id','name','roll_profrssion','active','profession_no')

    def get_num_profession_no(self, obj):
        return obj.num_profession_no() 
    


    # def create(self, validated_data):
    #     profession_no = validated_data['profession_no']
    #     del validated_data ['profession_no']
 
    #     Professions = Profession.objects.create(**validated_data)

    #     for i in profession_no:
    #         pro = student.objects.create(**i)
    #         Professions.profession_no.add(pro)
    #         Professions.save()
    #         return Professions

        
