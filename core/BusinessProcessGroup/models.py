from django.db import models
from django.utils.translation import ugettext_lazy as _


class BusinessProcessGroup(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'business_process_group'
        verbose_name_plural = _('02. Группы бизнес-процесов(BusinessProcessGroup)')

    def __str__(self):
        return "%s" % self.name

    @property
    def label(self):
        return self.name
