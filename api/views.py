from .models import Student
from .serializers import StudentSerializer
from utils.HttpErrors import HttpNotFound, HttpOK, HttpBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
# Create your views here.

# @api_view()
# def get_student(req, pk):
#     try:
#         stu = Student.objects.get(id=pk)
#         serializer = StudentSerializer(stu)
#         return Response(serializer.data)
#     except:
#         return HttpNotFound('Student Not Found')


# @api_view()
# def get_students(req):

#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu, many=True)
#     return Response(serializer.data)


# @csrf_exempt
# @api_view(['POST'])
# def create_student(req):
#     body = req.data
#     serializer = StudentSerializer(data=body)
#     if serializer.is_valid():
#         serializer.save()
#         return HttpOK('Student Created!')
#     else:
#         return HttpBadRequest(serializer.errors)


# @csrf_exempt
# @api_view(['PUT'])
# def update_student(req, id):
#     try:
#         body = req.data
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data=body)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpOK('Student Updated!')
#         else:
#             return HttpBadRequest(serializer.errors)
#     except:

#         return HttpNotFound('Student Not Found')


# @csrf_exempt
# @api_view(['DELETE'])
# def delete_student(req, id):
#     try:
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         return HttpOK('Student Deleted!')
#     except:
#         return HttpNotFound('Student Not Found!')

# List And Create - Primary Key (pk) Param Not Required
# class StudentLCAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, req, *args, **kwargs):
#         return self.list(req, *args, **kwargs)

#     def post(self, req, *args, **kwargs):
#         return self.create(req, *args, **kwargs)


# # Retreive Update And Delete - Primary Key (pk) Required
# class StudentGPD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, req, *args, **kwargs):
#         return self.retrieve(req, *args, **kwargs)

#     def put(self, req, *args, **kwargs):
#         return self.update(req, *args, **kwargs)

#     def delete(self, req, *args, **kwargs):
#         return self.destroy(req, *args, **kwargs)

# class StudentLCAPI(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentGPD(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentViewSet(viewsets.ViewSet):
    def list(self, req):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, req, pk=None):
        try:
            id = pk
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        except:
            return HttpNotFound('Student Not Found')

    def create(self, req):
        body = req.data
        serializer = StudentSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return HttpOK('Student Created!')
        else:
            return HttpBadRequest(serializer.errors)

    def update(self, req, pk=None):
        try:
            id = pk
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

    def destroy(self, req, pk=None):
        try:
            id = pk
            stu = Student.objects.get(id=id)
            stu.delete()
            return HttpOK('Student Deleted!')
        except:
            return HttpNotFound('Student Not Found!')
