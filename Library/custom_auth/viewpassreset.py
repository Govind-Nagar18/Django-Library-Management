from rest_framework.decorators import api_view, permission_classes
from django.core.cache import cache
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
import random

# ⬇️ 1. Send OTP
@api_view(['POST'])
@permission_classes([AllowAny])
def Send_reset_otp(request):
    email = request.data.get('email')
    
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return Response({'error': 'No account with this email'}, status=status.HTTP_404_NOT_FOUND)

    otp = str(random.randint(100000, 999999))
    cache.set(f'reset_otp_{email}', otp, timeout=300)  # Cache for 5 minutes

    send_mail(
        'Password Reset OTP',
        f'Your OTP is: {otp}',
        'noreply@yourdomain.com',
        [email],
        fail_silently=False,
    )

    return Response({'message': 'OTP sent to your email'}, status=status.HTTP_200_OK)


# ⬇️ 2. Verify OTP
@api_view(['POST'])
@permission_classes([AllowAny])
def Verify_reset_otp(request):
    email = request.data.get('email')
    otp = request.data.get('otp')

    cached_otp = cache.get(f'reset_otp_{email}')
    if not cached_otp or cached_otp != otp:
        return Response({'error': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'OTP verified. You can now reset your password.'}, status=status.HTTP_200_OK)


# ⬇️ 3. Reset Password
@api_view(['POST'])
@permission_classes([AllowAny])
def Reset_password(request):
    email = request.data.get('email')
    new_password = request.data.get('new_password')

    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    user.set_password(new_password)
    user.save()

    cache.delete(f'reset_otp_{email}')  # Clear OTP after success

    return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)
