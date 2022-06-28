from django.urls import path
from .views import UserRegister, DevicesListView, DeviceView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',UserRegister.as_view(),name='Users registration Endpoint'),
    path('devices/',DevicesListView.as_view(),name='List of all devices'),
    path('devices/<str:id>',DeviceView.as_view(),name='Device details')
]