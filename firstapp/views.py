from django.shortcuts import render
from firstapp.models import Employee
from rest_framework.decorators import api_view
from .serializers import Employeeserializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class EmployeeList(APIView):
    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = Employeeserializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Employeeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Employee_list(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Employeeserializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Employeeserializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
