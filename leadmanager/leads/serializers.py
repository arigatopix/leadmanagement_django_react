# สร้าง object เป็น json, xml
from rest_framework import serializers
from leads.models import Lead

# Lead Serializer


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        """เอาข้อมูลมาจาก models Lead """
        model = Lead
        fields = '__all__'
