# from django.db import models
# from django.utils import timezone
#
# from core.Enterprise.models import Enterprise
# from core.BusinessProcessGroup.models import BusinessProcessGroup
#
#

#


#

#
# class ProcessExecutor(models.Model):
#     department = models.ForeignKey(Department, on_delete=models.PROTECT)
#     business_process = models.ForeignKey(BusinessProcess, on_delete=models.PROTECT)
#     employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
#
#     class Meta:
#         db_table = 'process_executor'
#         unique_together = ('department', 'business_process')
#         verbose_name_plural = ('07. Исполнители процессов(ProcessExecutor)')
#
#     def __str__(self):
#         return 'ProcessExecutor: %s' % self.id
#
#
# '''
# DEFINITION BUSINESS PROCESS
# '''
#
#
# class ArrowType(models.Model):
#     name = models.CharField(max_length=32)
#     short_name = models.CharField(max_length=1)
#
#     class Meta:
#         db_table = 'arrow_type'
#         verbose_name_plural = ('08. Типы стрелок(ArrowType)')
#
#     def __str__(self):
#         return 'Type: %s' % self.short_name
#
#
# class GlossaryArrow(models.Model):
#     arrow_description = models.CharField(max_length=64)
#     type = models.ForeignKey(ArrowType, on_delete=models.PROTECT)
#
#     class Meta:
#         db_table = 'glossary_arrow'
#         verbose_name_plural = ('09. Глоссарий стрелок(GlossaryArrow)')
#
#     def __str__(self):
#         return '%s' % self.arrow_description
#
#
# class BusinessProcessWork(models.Model):
#     name = models.CharField(max_length=32, null=True)
#     parent = models.CharField(max_length=32)
#     level = models.CharField(max_length=8)
#     process = models.ForeignKey(BusinessProcess, on_delete=models.PROTECT)
#
#     class Meta:
#         db_table = 'business_process_work'
#         verbose_name_plural = ('10. Работы бизнес-процессов(BusinessProcessWork)')
#
#     def __str__(self):
#         return 'Name: %s. Parent: %s' % self.name, self.parent
#
#
# class ArrowWork(models.Model):
#     work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
#     arrow = models.ForeignKey(GlossaryArrow, on_delete=models.PROTECT)
#     specification = models.CharField(max_length=128)
#
#     class Meta:
#         db_table = 'arrow_work'
#         unique_together = ('work', 'arrow')
#         verbose_name_plural = ('11. Стрелки работ(ArrowWork)')
#
#     def __str__(self):
#         return 'Arrow: %s to Work: %s' % self.arrow, self.work
#
#
# class TypeResource(models.Model):
#     name = models.CharField(max_length=32)
#
#     class Meta:
#         db_table = 'type_resource'
#         verbose_name_plural = ('12. Типы ресурсов(TypeResource)')
#
#     def __str__(self):
#         return 'Type: %s' % self.name
#
#
# class ScaleMeasure(models.Model):
#     name = models.CharField(max_length=32)
#
#     class Meta:
#         db_table = 'scale_measure'
#         verbose_name_plural = ('13. Шкала измерений(ScaleMeasure)')
#
#     def __str__(self):
#         return 'Scale: %s' % self.name
#
#
# class UnitMeasure(models.Model):
#     name = models.CharField(max_length=16)
#     scale = models.ForeignKey(ScaleMeasure, on_delete=models.PROTECT)
#
#     class Meta:
#         db_table = 'unit_measure'
#         verbose_name_plural = ('14. Единицы измерений(UnitMeasure)')
#
#     def __str__(self):
#         return 'Unit measure: %s %s' % self.name, self.scale
#
#
# class Resource(models.Model):
#     name = models.CharField(max_length=32)
#     cost = models.DecimalField(decimal_places=4, max_digits=6)
#     type = models.ForeignKey(TypeResource, on_delete=models.PROTECT)
#     measure = models.ForeignKey(UnitMeasure, on_delete=models.PROTECT)
#
#     class Meta:
#         db_table = 'resource'
#         verbose_name_plural = ('15. Ресурсы(Resource)')
#
#     def __str__(self):
#         return 'Resource: %s - Cost:%s' % self.name, self.cost
#
#
# class WorkResource(models.Model):
#     work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
#     resource = models.ForeignKey(Resource, on_delete=models.PROTECT)
#     expense = models.DecimalField(decimal_places=4, max_digits=6)
#
#     class Meta:
#         db_table = 'work_resource'
#         unique_together = ('work', 'resource')
#         verbose_name_plural = ('16. Ресурсы работ(WorkResource)')
#
#     def __str__(self):
#         return 'Work: %s - Resource: %s' % self.work, self.resource
#
#
# '''
# INDICATOR AND ANALYSIS
# '''
#
#
# class Analysis(models.Model):
#     description = models.CharField(max_length=128)
#     create_at = models.DateTimeField(default=timezone.now)
#
#     class Meta:
#         db_table = 'analysis'
#         verbose_name_plural = '17. Анализ(Analysis)'
#
#     def __str__(self):
#         return 'ID: %s' % self.id
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
