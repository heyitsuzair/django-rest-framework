from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', views.get_students),
    path('stuinfo/<int:pk>', views.get_student),
    path('create-student', views.create_student),
]
