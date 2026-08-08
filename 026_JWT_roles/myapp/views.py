from django.shortcuts import render
from rest_framework.response import Response
from myapp.serializer import *
from rest_framework.decorators import api_view,permission_classes
from myapp.permissions import *
from rest_framework.permissions import *

@api_view(['POST'])
def reg(request):
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response({"message":"Registration successfully"})
    else:
        return Response({"error":ser.errors})
    
@api_view(['GET'])
@permission_classes([IsStudent])
def get_student(request):
    return Response("st api calling")

@api_view(['GET'])
@permission_classes([IsFaculty])
def get_faculty(request):
    return Response("ft api calling")

@api_view(['GET'])
@permission_classes([AllowAny])
def get_normal(request):
    return Response("normal api calling")