from django.db import models

'''
ENTERPRISE
'''


class Enterprise(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'enterprise'

    def __str__(self):
        return "ID:{0} - {1}".format(self.id, self.name)

    @property
    def label(self):
        return self.name


class BusinessProcessGroup(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'business_process_group'

    def __str__(self):
        return "ID:{0} - {1}".format(self.id, self.name)

    @property
    def label(self):
        return self.name


class BusinessProcess(models.Model):
    name = models.CharField(max_length=128)
    cost = models.FloatField()
    relative_important = models.FloatField()
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT)
    bp_group = models.ForeignKey(BusinessProcessGroup, on_delete=models.PROTECT)

    class Meta:
        db_table = 'business_process'

    def __str__(self):
        return "ID:{0} - {1}".format(self.id, self.name)

    @property
    def label(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=64)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return "Отдел {1} - id:{0}".format(self.id, self.name)


class PositionEmployee(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'position_employee'

    def __str__(self):
        return '{0} - id:{1}'.format(self.name, self.id)


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    patronymic = models.CharField(max_length=64)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    position_employee = models.ForeignKey(PositionEmployee, on_delete=models.PROTECT)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return '{2} {1} - id:{0}'.format(self.id, self.first_name, self.last_name)


class ProcessExecutor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    business_process = models.ForeignKey(BusinessProcess, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    class Meta:
        db_table = 'process_executor'
        unique_together = ('department', 'business_process')

    def __str__(self):
        return 'ProcessExecutor: %s' % self.id


'''
DEFINITION BUSINESS PROCESS
'''


class ArrowType(models.Model):
    name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=1)

    class Meta:
        db_table = 'arrow_type'

    def __str__(self):
        return 'Type: %s' % self.short_name


class GlossaryArrow(models.Model):
    arrow_description = models.CharField(max_length=64)
    type = models.ForeignKey(ArrowType, on_delete=models.PROTECT)

    class Meta:
        db_table = 'glossary_arrow'

    def __str__(self):
        return '%s' % self.arrow_description


class BusinessProcessWork(models.Model):
    name = models.CharField(max_length=32, null=True)
    parent = models.CharField(max_length=32)
    level = models.CharField(max_length=8)
    process = models.ForeignKey(BusinessProcess, on_delete=models.PROTECT)

    class Meta:
        db_table = 'business_process_work'

    def __str__(self):
        return 'Name: %s. Parent: %s' % self.name, self.parent


class ArrowWork(models.Model):
    work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
    arrow = models.ForeignKey(GlossaryArrow, on_delete=models.PROTECT)
    specification = models.CharField(max_length=128)

    class Meta:
        db_table = 'arrow_work'
        unique_together = ('work', 'arrow')

    def __str__(self):
        return 'Arrow: %s to Work: %s' % self.arrow, self.work


class TypeResource(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'type_resource'

    def __str__(self):
        return 'Type: %s' % self.name


class ScaleMeasure(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'scale_measure'

    def __str__(self):
        return 'Scale: %s' % self.name


class UnitMeasure(models.Model):
    name = models.CharField(max_length=16)
    scale = models.ForeignKey(ScaleMeasure, on_delete=models.PROTECT)

    class Meta:
        db_table = 'unit_measure'

    def __str__(self):
        return 'Unit measure: %s %s' % self.name, self.scale


class Resource(models.Model):
    name = models.CharField(max_length=32)
    cost = models.DecimalField(decimal_places=4, max_digits=6)
    type = models.ForeignKey(TypeResource, on_delete=models.PROTECT)
    measure = models.ForeignKey(UnitMeasure, on_delete=models.PROTECT)

    class Meta:
        db_table = 'resource'

    def __str__(self):
        return 'Resource: %s - Cost:%s' % self.name, self.cost


class WorkResource(models.Model):
    work = models.ForeignKey(BusinessProcessWork, on_delete=models.PROTECT)
    resource = models.ForeignKey(Resource, on_delete=models.PROTECT)
    expense = models.DecimalField(decimal_places=4, max_digits=6)

    class Meta:
        db_table = 'work_resource'
        unique_together = ('work', 'resource')

    def __str__(self):
        return 'Work: %s - Resource: %s' % self.work, self.resource
