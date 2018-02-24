from django import template

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.Department.models import Department
from core.PositionEmployee.models import PositionEmployee


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    patronymic = models.CharField(max_length=64)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    position_employee = models.ForeignKey(PositionEmployee, on_delete=models.PROTECT)

    class Meta:
        db_table = 'employee'
        verbose_name_plural = _('06. (Employee)')

    def __str__(self):
        return '{1} {0}'.format(self.first_name, self.last_name)

    register = template.Library()

    @register.simple_tag
    def model_name_plural(value):
        '''
        Django template filter which returns the plural verbose name of a model.
        '''
        if hasattr(value, 'model'):
            value = value.model

        return value._meta.verbose_name_plural.title()

    @register.simple_tag
    def model_name(value):
        '''
        Django template filter which returns the verbose name of a model.
        '''
        if hasattr(value, 'model'):
            value = value.model

        return value._meta.verbose_name.title()
