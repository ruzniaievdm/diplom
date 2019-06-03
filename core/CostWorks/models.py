from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.Analysis.models import Analysis
from core.AnalysisProcess.models import AnalysisProcess
from core.BusinessProcess.models import BusinessProcess
from core.BusinessProcessWork.models import BusinessProcessWork


class CostWorks(models.Model):
    unique_cw = models.ForeignKey(AnalysisProcess, related_name='cost_works', on_delete=models.PROTECT)
    work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
    kind = models.CharField(max_length=64, null=True, blank=True)
    cost_work = models.FloatField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = _('cost_works')
        verbose_name_plural = _('Cost works')
        unique_together = ('unique_cw', 'work')

    def __str__(self):
        return '%s' % self.work.name
