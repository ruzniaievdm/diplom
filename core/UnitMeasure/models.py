from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.ScaleMeasure.models import ScaleMeasure


class UnitMeasure(models.Model):
    name = models.CharField(max_length=16)
    scale = models.ForeignKey(ScaleMeasure, on_delete=models.PROTECT)

    class Meta:
        db_table = 'unit_measure'
        verbose_name_plural = _('14. (UnitMeasure)')

    def __str__(self):
        return '%s' % self.name


