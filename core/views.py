from .models import Device, User
from .serializers import UserSerializer, DeviceSerializer
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class UserRegister(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DevicesListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.validated_data["owner"] = self.request.user
        return super().perform_create(serializer)
    



class DeviceView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DeviceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return Device.objects.filter(owner=self.request.user)
    