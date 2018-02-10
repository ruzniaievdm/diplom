from django.contrib import admin
from .models import *


class BusinessProcessInline(admin.TabularInline):
    model = BusinessProcess


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    inlines = [BusinessProcessInline]


@admin.register(BusinessProcess)
class BusinessProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'relative_important', 'enterprise', 'bp_group')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'department', 'position_employee')


admin.site.register(BusinessProcessGroup)
admin.site.register(Department)
admin.site.register(PositionEmployee)
admin.site.register(ProcessExecutor)
# DefinitionBusinessProcess
admin.site.register(ArrowType)
admin.site.register(GlossaryArrow)
admin.site.register(BusinessProcessWork)
admin.site.register(ArrowWork)
admin.site.register(TypeResource)
admin.site.register(ScaleMeasure)
admin.site.register(UnitMeasure)
admin.site.register(Resource)
admin.site.register(WorkResource)
