from django.db import models
from django.utils.translation import ugettext_lazy as _


class TypeResource(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'type_resource'
        verbose_name_plural = ('12. (TypeResource)')

    def __str__(self):
        return '%s' % self.name
