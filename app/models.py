from django.db import models


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
    bp_process = models.ManyToManyField(BusinessProcess, through='ProcessExecutor', through_fields=('department', 'business_process'))

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
