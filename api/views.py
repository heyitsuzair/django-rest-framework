from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from utils.HttpErrors import HttpNotFound, HttpOK, HttpBadRequest
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view()
def get_student(req, pk):
    try:
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)
    except:
        return HttpNotFound('Student Not Found')


@api_view()
def get_students(request):

    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def create_student(req):
    body = req.data
    serializer = StudentSerializer(data=body)
    if serializer.is_valid():
        serializer.save()
        return HttpOK('Student Created!')
    else:
        return HttpBadRequest(serializer.errors)


@csrf_exempt
@api_view(['PUT'])
def update_student(req, id):
    try:
        body = req.data
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=body)
        if serializer.is_valid():
            serializer.save()
            return HttpOK('Student Updated!')
        else:
            return HttpBadRequest(serializer.errors)
    except:

        return HttpNotFound('Student Not Found')


@csrf_exempt
@api_view(['DELETE'])
def delete_student(req, id):
    try:
        stu = Student.objects.get(id=id)
        stu.delete()
        return HttpOK('Student Deleted!')
    except:
        return HttpNotFound('Student Not Found!')
