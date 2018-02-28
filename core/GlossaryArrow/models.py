from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.ArrowType.models import ArrowType


class GlossaryArrow(models.Model):
    arrow_description = models.CharField(max_length=64)
    type = models.ForeignKey(ArrowType, on_delete=models.PROTECT)

    class Meta:
        db_table = 'glossary_arrow'
        verbose_name_plural = _('09. (GlossaryArrow)')

    def __str__(self):
        return '%s' % self.arrow_description
