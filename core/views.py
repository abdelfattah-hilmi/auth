from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer

class UserRegister(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
