# coding=utf-8
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from core.BusinessProcessWork.models import BusinessProcessWork
from .serializers import BusinessProcessWorkSerializer


class BusinessProcessWorkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BusinessProcessWorkSerializer
    queryset = BusinessProcessWork.objects.all()

    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    def get_queryset(self):
        queryset = self.queryset
        params = self.request.query_params
        process = params.get('process', None)
        if process:
            queryset = queryset.filter(process=process)
        return queryset
