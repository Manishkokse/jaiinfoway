from django.shortcuts import render

# Create your views here.

from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET'])

def employee_list(request):
    employee=Employee.objects.all()
    serializer = EmployeeSerializer(employee,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def employee_detail(request, pk):
    try: 
        employee = Employee.objects.get(pk=pk) 
    except Employee.DoesNotExist: 
        return Response({'message': 'The Employee does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)

@api_view(['POST'])
def employee_create(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def employee_update(request, pk):
    try: 
        employee = Employee.objects.get(pk=pk) 
        serializer = EmployeeSerializer(instance=employee,data=request.data)
    except Employee.DoesNotExist: 
        return Response({'message': 'The Employee does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def employee_delete(request, pk):
    try: 
        employee = Employee.objects.get(pk=pk)
        employee.delete() 
    except Employee.DoesNotExist: 
        return Response({'message': 'The Employee does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    return Response({'message': 'Employee was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
