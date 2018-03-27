from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from core.BusinessProcessGroup.models import BusinessProcessGroup
from core.Enterprise.models import Enterprise


class BusinessProcess(models.Model):
    name = models.CharField(max_length=128)
    cost_plan = models.FloatField()
    relative_important = models.FloatField()
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT)
    bp_group = models.ForeignKey(BusinessProcessGroup, on_delete=models.PROTECT)

    class Meta:
        db_table = 'business_process'
        verbose_name_plural = _('03. BusinessProcess')

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('work-update', kwargs={'pk': self.pk})

    @property
    def label(self):
        return self.name

#
#
# class WorkAnalysis(models.Model):
#     work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
#     analysis = models.ForeignKey(Analysis, on_delete=models.PROTECT)
#     cost = models.FloatField()
#     execution_time = models.CharField(max_length=32)
#     relative_importance = models.FloatField()
#     relative_cost = models.FloatField()
#     measure = models.ForeignKey(UnitMeasure, on_delete=models.PROTECT)
#
#     class Meta:
#         unique_together = ('work', 'analysis')
#         db_table = 'work_analysis'
#         verbose_name_plural = ('18. Анализ работ(WorkAnalysis)')
#
#     def __str__(self):
#         return 'ID analysis: %s - Work: %s' % self.analysis, self.work
#
#
# class GroupIndicator(models.Model):
#     name = models.CharField(max_length=64)
#
#     class Meta:
#         db_table = 'group_indicator'
#         verbose_name_plural = ('19. Группы индикаторов(GroupIndicator)')
#
#     def __str__(self):
#         return '%s' % self.name
#
#
# class Factor(models.Model):
#     name = models.CharField(max_length=64)
#
#     class Meta:
#         db_table = 'factor'
#         verbose_name_plural = ('20. Влияющие факторы(Factor)')
#
#     def __str__(self):
#         return '%s ' % self.name
#
#
# class Indicator(models.Model):
#     name = models.CharField(max_length=64)
#     lower_limit = models.FloatField()
#     upper_limit = models.FloatField()
#     group = models.ForeignKey(GroupIndicator, on_delete=models.PROTECT)
#     factor = models.ForeignKey(Factor, on_delete=models.PROTECT)
#     measure = models.ForeignKey(UnitMeasure, on_delete=models.PROTECT)
#
#     class Meta:
#         db_table = 'indicator'
#         verbose_name_plural = ('21. Показатели(Indicator)')
#
#     def __str__(self):
#         return 'Name: %s' % self.name
#
#         # class Recommendation(models.Model):
#         #     analysis = models.ForeignKey(WorkAnalysis, on_delete=models.PROTECT)
#         #     work = models.ForeignKey(WorkAnalysis, on_delete=models.PROTECT)
#         #     measure = models.ForeignKey(UnitMeasure, on_delete=models.PROTECT)
#         #     recommend_cost = models.FloatField()
#         #     recommend_execution_time = models.CharField(max_length=64)
#         #     relative_cost = models.FloatField()
#         #     relative_execution_time = models.CharField(max_length=64)
#         #
#         #     class Meta:
#         #         db_table = 'recommendation'
#         #         unique_together = ('analysis', 'work', 'measure')
#         #         verbose_name_plural = ('22. Выработка рекомендаций(Recommendation)')
#
# #
# #     def __str__(self):
# #         return 'Work: %s - cost: %s, time: %s' % self.work, self.recommend_cost, self.recommend_execution_time
