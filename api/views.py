from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
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
    print(stu)
    serializer = StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return HttpOK('Student Created!')
        else:
            return HttpBadRequest(serializer.errors)
