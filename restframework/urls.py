from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', views.StudentLCAPI.as_view()),
    path('stuinfo/<int:pk>', views.StudentGPD.as_view()),
]
