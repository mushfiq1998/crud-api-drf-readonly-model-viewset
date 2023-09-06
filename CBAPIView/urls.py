from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# creating router object
router = DefaultRouter()

# Registre StudentViewSet class with Router
router.register('studentapi', views.StudentReadOnlyModelViewset, 
                basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]