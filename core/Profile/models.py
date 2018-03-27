from django.db import models
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'profile'
        verbose_name_plural = _('777. (Profile)')


class FamilyMember(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)

    class Meta:
        db_table = 'family'
        verbose_name_plural = _('777. (Family)')
