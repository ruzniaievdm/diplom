from django.contrib import admin

from core.CostWork.models import CostWork


class CostWorkInline(admin.StackedInline):
    model = CostWork




admin.site.register(CostWork)
