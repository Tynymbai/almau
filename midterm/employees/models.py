from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='full_name')
    position = models.CharField(max_length=255, verbose_name='position')
    salary = models.IntegerField(max_length=100, verbose_name='salary')

    class Meta:
        verbose_name = 'employees'
        verbose_name_plural = 'Employee'

    def __str__(self):
        return self.full_name
