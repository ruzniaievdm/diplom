from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.BusinessProcess.models import BusinessProcess
from core.Department.models import Department
from core.Employee.models import Employee


class ProcessExecutor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    business_process = models.ForeignKey(BusinessProcess, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    class Meta:
        db_table = 'process_executor'
        unique_together = ('department', 'business_process')
        verbose_name_plural = _('07. (ProcessExecutor)')

    def __str__(self):
        return 'Исполнители процесса: %s' % self.id
