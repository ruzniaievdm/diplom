from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.Analysis.models import Analysis
from core.BusinessProcess.models import BusinessProcess


class AnalysisProcess(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.PROTECT)
    process = models.ForeignKey(BusinessProcess, on_delete=models.PROTECT)
    is_active_cost = models.BooleanField(default=False)
    is_active_importance = models.BooleanField(default=False)

    class Meta:
        db_table = 'analysis_process'
        verbose_name_plural = _('(AnalysisProcess)')
        unique_together = ('analysis', 'process')

    def __str__(self):
        return 'ID: %s' % self.id

# def insert():
