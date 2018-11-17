from rest_framework import serializers
from leads.models import LeadsModel

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadsModel
        # fields = ('id', 'name', 'email', 'message')
        fields = '__all__'