from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcessWork.models import BusinessProcessWork
from core.Resource.models import Resource


class WorkResource(models.Model):
    work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
    resource = models.ForeignKey(Resource, on_delete=models.PROTECT)
    expense = models.FloatField()


    class Meta:
        db_table = 'work_resource'
        unique_together = ('work', 'resource')
        verbose_name_plural = _('16. (WorkResource)')

    def __str__(self):
        return 'Work: %s - Resource: %s' % self.work, self.resource
