from django.db import models
from django.utils.translation import ugettext_lazy as _

from Manager import BusinessProcessWork
from core.BusinessProcess.models import BusinessProcess


class BusinessProcessWork(models.Model):
    level_of_choices = (
        (1, 'Lvl 1'),
        (2, 'Lvl 2'),
        (3, 'Lvl 3'),
        (4, 'Lvl 4'),
        (5, 'Lvl 5'),
        (6, 'Lvl 6'),
        (7, 'Lvl 7'),
    )

    name = models.CharField(max_length=64, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True, choices=level_of_choices)
    parent = models.CharField(max_length=64, null=True, blank=True)
    process = models.ForeignKey(BusinessProcess, on_delete=models.PROTECT)

    class Meta:
        db_table = 'business_process_work'
        verbose_name_plural = _('10. (BusinessProcessWork)')

    def __str__(self):
        return '%s' % self.name
