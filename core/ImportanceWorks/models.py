from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.AnalysisProcess.models import AnalysisProcess
from core.BusinessProcessWork.models import BusinessProcessWork


class ImportanceWorks(models.Model):
    unique = models.ForeignKey(AnalysisProcess, on_delete=models.PROTECT)
    work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
    elemental_importance = models.FloatField()
    object_importance = models.FloatField()
    relative_cost = models.FloatField(null=True, blank=True)
    relative_importance = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = _('importance_works')
        verbose_name_plural = _('Importance Works')
        unique_together = ('work', 'unique')

    def __str__(self):
        return '%s' % self.id
