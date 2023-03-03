from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse
from utils.HttpErrors import HttpNotFound, HttpOK, HttpBadRequest
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def get_student(request, pk):
    try:
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu)
        return JsonResponse(serializer.data)
    except:
        return HttpNotFound('Student Not Found')


def get_students(request):

    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def create_student(request):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = StudentSerializer(data=python_data)
    if serializer.is_valid():
        serializer.save()
        return HttpOK('Student Created!')
    else:
        return HttpBadRequest(serializer.errors)


@csrf_exempt
def update_student(request, id):
    try:
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return HttpOK('Student Updated!')
        else:
            return HttpBadRequest(serializer.errors)
    except:

        return HttpNotFound('Student Not Found')


@csrf_exempt
def delete_student(request, id):
    try:
        stu = Student.objects.get(id=id)
        stu.delete()
        return HttpOK('Student Deleted!')
    except:
        return HttpNotFound('Student Not Found!')
