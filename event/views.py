from rest_framework import generics
from .serializers import EventSerializer
from .models import Event


class EventListCreateAPIView (generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventRetrieveAPIView (generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDestroyAPIView (generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventUpdateAPIView (generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer