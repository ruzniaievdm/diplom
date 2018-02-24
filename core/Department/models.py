from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.Enterprise.models import Enterprise


class Department(models.Model):
    name = models.CharField(max_length=64)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT)

    class Meta:
        db_table = 'department'
        verbose_name_plural = _('04. (Department)')

    def __str__(self):
        return "%s" % self.name
