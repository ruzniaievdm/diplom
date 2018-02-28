from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcessGroup.models import BusinessProcessGroup
from core.Enterprise.models import Enterprise


class BusinessProcess(models.Model):
    name = models.CharField(max_length=128)
    cost_plan = models.FloatField()
    relative_important = models.FloatField()
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT)
    bp_group = models.ForeignKey(BusinessProcessGroup, on_delete=models.PROTECT)

    class Meta:
        db_table = 'business_process'
        verbose_name_plural = _('03. BusinessProcess')

    def __str__(self):
        return "%s" % self.name

    @property
    def label(self):
        return self.name
