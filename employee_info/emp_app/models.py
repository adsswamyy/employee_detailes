from django.db import models

# Create your models here.


class departments(models.Model):
    dept_no=models.CharField(unique=True,max_length=4,blank=False)
    dept_name=models.CharField(primary_key=True,max_length=40,blank=False)
    def __str__(self):
        return self.dept_name
class employee_no(models.Model):
    emp_no=models.IntegerField(primary_key=True,blank=False)


class titles(models.Model):
    emp_no=models.ForeignKey(employee_no,on_delete=models.CASCADE,related_name='employees_by_no',default='')
    title=models.CharField(primary_key=True,max_length=120)
    from_date=models.DateField(blank=False)
    to_date=models.DateField(blank=False)
    def __str__(self):
        return self.title
class salaries(models.Model):
    emp_no=models.ForeignKey(employee_no,on_delete=models.CASCADE,related_name='salaries_by_emp',default='')
    salary=models.CharField(max_length=3,blank=False)
    from_date=models.DateField(blank=True)
    to_date=models.DateField(blank=True)
    stitle=models.ForeignKey(titles,on_delete=models.CASCADE,related_name='salaries_by_title',default='')
    def __str__(self):
        return self.salary
class employees(models.Model):
    emp_no = models.ForeignKey(employee_no, on_delete=models.CASCADE, related_name='employees_by_emp_no',default='')
    birth_date = models.DateField(blank=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female')
        )
    gender = models.CharField(max_length=6, choices=gender_choices)
    hire_date = models.DateField(blank=False)
    dname = models.ForeignKey(departments, on_delete=models.CASCADE, related_name='employees_by_dnames', default='')
    etitle=models.ForeignKey(titles,on_delete=models.CASCADE,related_name='employee_by_titles',default='')
    salaries=models.ForeignKey(salaries,on_delete=models.CASCADE,related_name='employees_by_salaries',default='')


