from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Local


class LocalSerializer(serializers.HyperlinkedModelSerializer):
    locals = serializers.HyperlinkedRelatedField(
        view_name='local_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Local
        fields = ('id', 'name', 'city','state',)