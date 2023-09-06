from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# Code for CRUD
# In ModelViewSet queryset, serializer_class are two keywords variables
class StudentReadOnlyModelViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer