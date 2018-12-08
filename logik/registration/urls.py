from django.urls import path
from .views import SignUpView, ProfileUpdate

urlpatterns = [
    path('registro/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
]
