from django.db import models
from django.utils.translation import ugettext_lazy as _


class Analysis(models.Model):
    description = models.CharField(max_length=128)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'analysis'
        verbose_name_plural = _('17. (Analysis)')

    def __str__(self):
        return 'ID: %s' % self.id
