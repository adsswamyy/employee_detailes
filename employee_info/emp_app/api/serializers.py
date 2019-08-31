from rest_framework.serializers import ModelSerializer
from datetime import date
from emp_app.models import departments,employee_no,employees,titles,salaries

class departments_serializer(ModelSerializer):
    class Meta:
        model=departments
        fields='__all__'
class employee_no_serializer(ModelSerializer):
    class Meta:
        model=employee_no
        fields='__all__'

class employees_serializer(ModelSerializer):
    class Meta:
        model=employees
        fields='__all__'
class titles_serializer(ModelSerializer):
    class Meta:
        model=titles
        fields='__all__'
class salaries_serializer(ModelSerializer):
    class Meta:
        model=salaries
        fields='__all__'