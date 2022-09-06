from django.urls import path
from .views import UserRegister, DevicesListView, DeviceView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',TokenBlacklistView.as_view(), name='logout_view'),
    path('register/',UserRegister.as_view(),name='Users_registration_Endpoint'),
    path('devices/',DevicesListView.as_view(),name='List_of_all_devices'),
    path('devices/<str:id>',DeviceView.as_view(),name='Device_details'),
]