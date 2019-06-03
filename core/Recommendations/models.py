from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.AnalysisProcess.models import AnalysisProcess
from core.BusinessProcessWork.models import BusinessProcessWork
from core.Report.models import Report


class Recommendations(models.Model):
    unique = models.ForeignKey(AnalysisProcess, on_delete=models.PROTECT)
    work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
    report = models.ForeignKey(Report, on_delete=models.PROTECT, null=True)
    relative_cost = models.FloatField(null=True, blank=True)
    relative_importance = models.FloatField(null=True, blank=True)
    relative_duration = models.FloatField(null=True, blank=True)
    recommend_cost = models.FloatField(null=True, blank=True)
    recommend_duration = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = _('recommendations')
        verbose_name_plural = _('Recomendations')
        unique_together = ('work', 'unique')

    def __str__(self):
        return '%s' % self.id
