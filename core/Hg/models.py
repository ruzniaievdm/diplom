from django.db import models
from django.utils.translation import ugettext_lazy as _


class Hg(models.Model):
    arrow = models.CharField(max_length=64)

    class Meta:
        db_table = 'hg'
        verbose_name_plural = _('Hg')

    def __str__(self):
        return '%s' % self.arrow
