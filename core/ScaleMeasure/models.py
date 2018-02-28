from django.db import models
from django.utils.translation import ugettext_lazy as _


class ScaleMeasure(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'scale_measure'
        verbose_name_plural = _('13. (ScaleMeasure)')

    def __str__(self):
        return '%s' % self.name
