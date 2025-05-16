from django.urls import path
from .views import SignupView, LoginView, ProfileView,ProfileupdateView
from .viewpassreset import Send_reset_otp, Verify_reset_otp, Reset_password

urlpatterns = [
    path('signup/', SignupView.as_view(), name='Sign-up'),
    path('login/', LoginView.as_view(), name='Log-in'),
    path('profile/', ProfileView.as_view(), name='Profile-page'),
    path('profileupdate/', ProfileupdateView.as_view(), name='Profileupdate-page'),
    path('sendotp/', Send_reset_otp, name='sendotp' ),
    path('verifyotp/', Verify_reset_otp, name='verifyotp' ),
    path('resetpass/', Reset_password, name='resetpass' )

]