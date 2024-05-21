from rest_framework import serializers
from .models import (TypePoste, Grade, Profession, Employee, Poste, Department, AdresseEmployee, TypeProfession,
                     TypeDepartment)


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = "__all__"


class TypeProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProfession
        fields = "__all__"


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


class TypePosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePoste
        fields = "__all__"


class TypeDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDepartment
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class PosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class AdresseEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdresseEmployee
        fields = "__all__"








