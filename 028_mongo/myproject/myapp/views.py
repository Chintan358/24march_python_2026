from django.shortcuts import render
from myapp.mongodb import *
from django.http import JsonResponse
# Create your views here.


def index(request):
    students = list(category_collection.find())

    for student in students:
        student["_id"] = str(student["_id"])

    return JsonResponse(students, safe=False)