from rest_framework.viewsets import ModelViewSet
from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeViesSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ('post', 'get', 'delete', 'put')
