from rest_framework import generics
from .models import Clients
from .serializers import ClientsSerializer

class ClientCreateView(generics.CreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

class ClientUpdateView(generics.UpdateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    lookup_field = 'id'

class ClientDeleteView(generics.DestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    lookup_field = 'id'

class ClientDetailView(generics.RetrieveAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    lookup_field = 'id'
