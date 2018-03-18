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
