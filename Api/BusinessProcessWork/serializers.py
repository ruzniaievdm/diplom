# coding=utf-8
from rest_framework import serializers
from core.BusinessProcessWork.models import BusinessProcessWork


class SubBusinessProcessWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProcessWork
        fields = ('id', 'process', 'name', 'level', 'parent')


class BusinessProcessWorkSerializer(serializers.ModelSerializer):
    parent = SubBusinessProcessWorkSerializer()

    class Meta:
        model = BusinessProcessWork
        fields = ('id', 'process', 'name', 'level', 'parent')
