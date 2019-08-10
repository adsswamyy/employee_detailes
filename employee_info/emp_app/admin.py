from django.contrib import admin
from emp_app.models import employees,departments,dept_emp,titles,salaries
# Register your models here.
class employees_admin(admin.ModelAdmin):
    list_display = ['emp_no','birth_date','first_name','last_name','gender','hire_date']
admin.site.register(employees,employees_admin)

class departments_admin(admin.ModelAdmin):
    list_display = ['dept_no','dept_name']
admin.site.register(departments,departments_admin)

class dept_emp_admin(admin.ModelAdmin):
    list_display = ['emp_no','dept_no','from_date','to_date']
admin.site.register(dept_emp,dept_emp_admin)

class titles_admin(admin.ModelAdmin):
    list_display = ['emp_no','title','from_date','to_date']
admin.site.register(titles,titles_admin)

class salaries_admin(admin.ModelAdmin):
    list_display = ['emp_no','salary','from_date','to_date']
admin.site.register(salaries,salaries_admin)