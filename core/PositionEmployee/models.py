from django.db import models
from django.utils.translation import ugettext_lazy as _


class PositionEmployee(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'position_employee'
        verbose_name_plural = _('05. (PositionEmployee)')

    def __str__(self):
        return '%s' % self.name
