from django.contrib import admin
from emp_app.models import departments,employee_no,employees,titles,salaries
# Register your models here.
class departments_admin(admin.ModelAdmin):
    list_display = ['dept_no','dept_name']
admin.site.register(departments)
class employee_no_admin(admin.ModelAdmin):
    list_display = ['emp_no']
admin.site.register(employee_no,employee_no_admin)
class employees_admin(admin.ModelAdmin):
    list_display = ['emp_no','birth_date','first_name','last_name','gender','hire_date','dname']
admin.site.register(employees,employees_admin)
class titles_admin(admin.ModelAdmin):
    list_display = ['emp_no','title','from_date','to_date']
admin.site.register(titles,titles_admin)
class salaries_admin(admin.ModelAdmin):
    list_display = ['emp_no','salary','from_date','to_date','stitle']
admin.site.register(salaries,salaries_admin)




