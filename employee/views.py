from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import (TypePoste, Grade, Profession, Employee, Poste, Department, AdresseEmployee, TypeProfession,
                     TypeDepartment)
from .serializers import (EmployeeSerializer, GradeSerializer, AdresseEmployeeSerializer, DepartmentSerializer,
                          TypePosteSerializer, PosteSerializer, ProfessionSerializer, TypeProfessionSerializer,
                          TypeDepartmentSerializer)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    # def list(self, request, *args, **kwargs):
    #     return
    #
    # def update(self, request, *args, **kwargs):
    #     return

    def create(self, request, *args, **kwargs):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'grades': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return


class TypePosteViewSet(viewsets.ModelViewSet):
    queryset = TypePoste.objects.all()
    serializer_class = TypePosteSerializer

    # def list(self, request, *args, **kwargs):
    #     return
    #
    # def update(self, request, *args, **kwargs):
    #     return

    def create(self, request, *args, **kwargs):
        serializer = TypePosteSerializer(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'type_postes': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer

    # def list(self, request, *args, **kwargs):
    #     return
    #
    # def update(self, request, *args, **kwargs):
    #     return

    def create(self, request, *args, **kwargs):
        serializer = ProfessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'type_postes': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return


class TypeDepartmentViewSet(viewsets.ModelViewSet):
    queryset = TypeDepartment.objects.all()
    serializer_class = TypeDepartmentSerializer

    # def list(self, request, *args, **kwargs):
    #     return
    #
    # def update(self, request, *args, **kwargs):
    #     return

    def create(self, request, *args, **kwargs):
        serializer = TypeDepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'type_departments': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return


class TypeProfessionViewSet(viewsets.ModelViewSet):
    queryset = TypeProfession.objects.all()
    serializer_class = TypeProfessionSerializer

    def list(self, request, *args, **kwargs):
        data = TypeProfession.objects.all()
        serializer = TypeProfessionSerializer(data, many=True)
        return Response(data={'type_profession': serializer.data})

    # def update(self, request, *args, **kwargs):
    #     return

    def create(self, request, *args, **kwargs):
        serializer = TypeProfessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'type_profession': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # def list(self, request, *args, **kwargs):
    #     return
    #
    # def update(self, request, *args, **kwargs):
    #     return

    def create(self, request, *args, **kwargs):
        serializer = ProfessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'type_postes': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return


class PosteViewSet(viewsets.ModelViewSet):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer

    # def list(self, request, *args, **kwargs):
    #     return
    #
    # def update(self, request, *args, **kwargs):
    #     return

    def create(self, request, *args, **kwargs):
        serializer = PosteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'postes': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    # def list(self, request, *args, **kwargs):
    #     return
    #
    # def update(self, request, *args, **kwargs):
    #     return

    def create(self, request, *args, **kwargs):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès", 'departments': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return


class AdresseEmployeeViewSet(viewsets.ModelViewSet):
    queryset = AdresseEmployee.objects.all()
    serializer_class = AdresseEmployeeSerializer

    # def list(self, request, *args, **kwargs):
    #     return
    #
    # def update(self, request, *args, **kwargs):
    #     return

    def create(self, request, *args, **kwargs):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED,
                            data={"message": "Enregistrement réussi avec succès",
                                  'adresses_employees': serializer.data})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return
