from leads.models import LeadsModel
from leads.serializers import LeadSerializer
from rest_framework import generics

class LeadListCreate(generics.ListCreateAPIView):
    queryset = LeadsModel.objects.all()
    serializer_class = LeadSerializer
