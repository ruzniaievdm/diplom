from django.db import models
from django.utils.translation import ugettext_lazy as _


class Report(models.Model):
    description = models.CharField(max_length=128, null=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'report'
        verbose_name_plural = _('(Report)')

    def __str__(self):
        return 'ID: %s' % self.id
