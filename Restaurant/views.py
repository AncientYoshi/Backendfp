# views.py

from rest_framework import generics, viewsets
from .models import Menu,Booking
from .serializers import MenuSerializer , BookingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

@permission_classes([IsAuthenticated])
class MySecuredView(APIView):
    def get(self, request):
        # Your view logic here
        return Response({"message": "You are authenticated"})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]