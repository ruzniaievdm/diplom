from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcess.models import BusinessProcess


class BusinessProcessWork(models.Model):
    name = models.CharField(max_length=32, null=True)
    parent = models.CharField(max_length=32)
    level = models.CharField(max_length=8)
    process = models.ForeignKey(BusinessProcess, on_delete=models.PROTECT)

    class Meta:
        db_table = 'business_process_work'
        verbose_name_plural = _('10. (BusinessProcessWork)')

    def __str__(self):
        return '%s' % self.name
