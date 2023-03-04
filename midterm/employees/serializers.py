from rest_framework import serializers
from employees.models import Employee


class EmployeesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(min_length=5, max_length=25, allow_null=False)
    position = serializers.CharField(allow_null=False, allow_blank=False)
    salary = serializers.IntegerField(min_value=0, max_value=255, allow_null=False)

    def create(self, validated_data):
        employee = Employee(**validated_data)
        employee.save()
        return employee

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.position = validated_data.get('position', instance.position)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save()
        return instance
