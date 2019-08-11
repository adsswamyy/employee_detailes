from django.db import models

# Create your models here.


class departments(models.Model):
    dept_no=models.CharField(primary_key=True,max_length=4,blank=False)
    dept_name=models.CharField(unique=True,max_length=40,blank=False)
    def __str__(self):
        return self.dept_no
class titles(models.Model):
    emp_no=models.IntegerField()
    title=models.CharField(max_length=50,blank=False)
    from_date = models.DateField(primary_key=True,blank=False)
    to_date = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    def __str__(self):
        return self.title
class salaries(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    salary=models.CharField(max_length=5,blank=False)
    title=models.ForeignKey(titles,on_delete=models.CASCADE,related_name='titles',default='')
    from_date=models.DateField(primary_key=True,blank=False)
    to_date = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    def __str__(self):
        return self.salary
class employees(models.Model):
    emp_no=models.IntegerField(primary_key=True,blank=False)
    birth_date=models.DateField(auto_now_add=False,auto_now=False,blank=False)
    first_name=models.CharField(max_length=30,blank=False)
    last_name=models.CharField(max_length=30,blank=False)
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    hire_date=models.DateField(auto_now_add=False,auto_now=False,blank=False)
    dept_no=models.ForeignKey(departments,on_delete=models.CASCADE,related_name='employees_by_dept_no',default='')
    title=models.ForeignKey(titles,on_delete=models.CASCADE,related_name='employees_by_titles')

    def __int__(self):
        return self.emp_no


class dept_emp(models.Model):
    emp_no=models.ForeignKey(employees,on_delete=models.CASCADE,related_name='dept_emp_by_employees')
    dept_no=models.ForeignKey(departments,on_delete=models.CASCADE,related_name='dept_emp_by_departments')
    from_date=models.DateField(primary_key=True,auto_now_add=False,auto_now=False,blank=False,default='2015')
    to_date=models.DateField(auto_now_add=False,auto_now=False,blank=False)









