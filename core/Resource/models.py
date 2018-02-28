from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.TypeResource.models import TypeResource
from core.UnitMeasure.models import UnitMeasure


class Resource(models.Model):
    name = models.CharField(max_length=32)
    cost = models.FloatField()
    type = models.ForeignKey(TypeResource, on_delete=models.PROTECT)
    measure = models.ForeignKey(UnitMeasure, on_delete=models.PROTECT)

    class Meta:
        db_table = 'resource'
        verbose_name_plural = _('15. (Resource)')

    def __str__(self):
        return '%s' % self.name
