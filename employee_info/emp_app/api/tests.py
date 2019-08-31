from rest_framework import APITestCase
from emp_app.models import employees,departments
# Create your tests here.
class employees_APITestCase(APITestCase):
    def setup(self):
        employees.objects.create(emp_no='01',birth_date="1990-01-05",first_name='swamy',last_name='ads',gender='male',hire_date="2019-01-05")

    def test_post_method_sucuess(self):
        url='http://127.0.0.1:8000/emp_app/emp_api/'
        data={'emp_no':'01',
              'birth_date':"1990-01-05",
              'first_name':'swamy',
              'last_name':'ads',
              'gender':'male',
              'hire_date':"2019-01-05"

        }
        response=self.client.post(url,data,format='json')
        print(response.status_code)
        self.assertEqual(response.status_code,201)
    def setup(self):
        employees.objects.create(emp_no='01', birth_date="1990-01-05", first_name='swamy', last_name='ads',gender='male', hire_date="2019-01-05")

    def test_get_method_sucuess(self):
        url = 'http://127.0.0.1:8000/emp_app/get_api/'
        response=self.client.get(url,data,format='json')
        self.assertEqual(response.status_code, 201)
        qs=employees.objects.filter(first_name='swamy')
        self.assertEqual(qs,count(),1)


