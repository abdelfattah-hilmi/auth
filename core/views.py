from .models import User
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated


class UserRegister(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
