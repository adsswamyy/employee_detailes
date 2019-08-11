from rest_framework.serializers import ModelSerializer
from datetime import date
from emp_app.models import employees,departments,dept_emp,titles,salaries

class dept_emp_serializer(ModelSerializer):
    class Meta:
        model=dept_emp
        fields='__all__'
class titles_serializers(ModelSerializer):
    class Meta:
        model=titles
        fields='__all__'
class salary_serializers(ModelSerializer):
    class Meta:
        model=salaries
        fields='__all__'

class employees_serializer(ModelSerializer):
    dept_emp_by_employees=dept_emp_serializer(read_only=True,many=True)
    titles_by_employees=titles_serializers(read_only=True,many=True)
    employees_by_salaries=salary_serializers(read_only=True,many=True)
    def age_validation(birthdate):
        today=date.today()
        age=today.year-birthdate.year-((today.month,today.day)<(birthdate.month,birthdate.day))
        if (not(18<age<60)):
            raise ModelSerializer.ValidationError('not eligibal for this employee')
        return birthdate
    class Meta:
        model=employees
        fields='__all__'

class departments_serializer(ModelSerializer):
    dept_emp_by_departments=dept_emp_serializer(read_only=True,many=True)
    employees_by_dept_no=employees_serializer(read_only=True,many=True)
    class Meta:
        model=departments
        fields='__all__'

