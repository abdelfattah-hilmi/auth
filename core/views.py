from .models import Device, User
from .serializers import UserSerializer, DeviceSerializer
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class UserRegister(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DevicesListView(ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceView(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'