from django.db import models
from django.utils.translation import ugettext_lazy as _


class Enterprise(models.Model):
    """
    Enterprise
    """
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'enterprise'
        verbose_name_plural = _('01. Enterprise')

    def __str__(self):
        return "ID:{0} - {1}".format(self.id, self.name)

    @property
    def label(self):
        return self.name
