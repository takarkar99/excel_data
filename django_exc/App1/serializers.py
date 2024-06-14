from rest_framework import serializers
from .models import ExcelData



class ExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelData
        fields = '__all__'