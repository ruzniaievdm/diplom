from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcessWork.models import BusinessProcessWork
from core.GlossaryArrow.models import GlossaryArrow


class ArrowWorks(models.Model):
    arrow = models.ForeignKey(GlossaryArrow, on_delete=models.PROTECT)
    work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
    description = models.CharField(max_length=64)

    class Meta:
        db_table = 'arrow_works'
        verbose_name_plural = _('(ArrowWorks)')
        unique_together = ('arrow', 'work')

    def __str__(self):
        return 'ID: %s' % self.id


