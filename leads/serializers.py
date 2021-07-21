from rest_framework import serializers
from .models import Lead


class LeadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'course', 'interest')


class LeadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('name', 'email', 'course', 'interest')
