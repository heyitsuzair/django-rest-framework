from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from utils.HttpErrors import HttpNotFound

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
    print(stu)
    serializer = StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data,safe=False)
