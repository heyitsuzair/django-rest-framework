from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register Student View Set With Router
router.register('stuinfo', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
    # path('stuinfo/', views.StudentLCAPI.as_view()),
    # path('stuinfo/<int:pk>', views.StudentGPD.as_view()),
]
