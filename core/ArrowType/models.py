from django.db import models
from django.utils.translation import ugettext_lazy as _


class ArrowType(models.Model):
    name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=2)

    class Meta:
        db_table = 'arrow_type'
        verbose_name_plural = _('08. (ArrowType)')

    def __str__(self):
        return 'Type: %s' % self.short_name
