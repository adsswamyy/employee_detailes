from django.shortcuts import render
from emp_app.api.serializers import employees_serializer
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from emp_app.models import employees
# Create your views here.
class post_api_employees(CreateAPIView):
    serializer_class = employees_serializer
    queryset = employees.objects.all()
class get_api_employees(RetrieveAPIView):
    serializer_class = employees_serializer
    queryset = employees.objects.all()












