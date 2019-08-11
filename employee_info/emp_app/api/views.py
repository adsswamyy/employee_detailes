from django.shortcuts import render
from emp_app.api.serializers import employees_serializer,salary_serializers,departments_serializer,titles_serializers
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from emp_app.models import employees,salaries,departments,titles
# Create your views here.
class post_api_employees(CreateAPIView):
    serializer_class = employees_serializer
    queryset = employees.objects.all()











