from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.Analysis.models import Analysis
from core.BusinessProcess.models import BusinessProcess
from core.BusinessProcessWork.models import BusinessProcessWork
from core.UnitMeasure.models import UnitMeasure


class CostWork(models.Model):
    process = models.ForeignKey(BusinessProcess, on_delete=models.PROTECT, null=True, blank=True)
    analysis = models.ForeignKey(Analysis, on_delete=models.PROTECT)
    work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
    kind = models.CharField(max_length=64, null=True, blank=True)
    measure = models.ForeignKey(UnitMeasure, on_delete=models.PROTECT, null=True, blank=True)
    cost_work = models.FloatField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'cost_work'
        verbose_name_plural = _('Cost work')
        unique_together = ('analysis', 'process')

    def __str__(self):
        return '%s' % self.work


class Coefficient(models.Model):
    name = models.CharField(max_length=12)
    value = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'coefficient'

    def __str__(self):
        return 'Coefficient id = %s' % self.id

    @property
    def label(self):
        return '%s: %s' % (self.name, self.value)

    def get_tuple(self):
        return self.name, self.value
