from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response

class SignupView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        image = request.FILES.get('image')
        phone = request.data.get('phone')

        if not username or not password:
            return Response({"Message":"Username and Password Required "}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(email=email).exists():
            return Response({"message":"Email already exists "}, status=status.HTTP_400_BAD_REQUEST)
        
        if CustomUser.objects.filter(username=username).exists():
            return Response({"message":"Username already exists "}, status=status.HTTP_400_BAD_REQUEST)
        
        user = CustomUser(username=username, email=email, phone=phone, image=image)
        user.set_password(password)
        user.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
            'message':'Account Create Successfully'
        },status=status.HTTP_202_ACCEPTED)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
            'message':'Log in successfully'
            },status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)




class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response({
            'username': user.username,
            'email': user.email,
            'phone': user.phone,
            'image': request.build_absolute_uri(user.image.url) if user.image else None,
        })


class ProfileupdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user

        user.username = request.data.get('username', user.username)
        user.phone = request.data.get('phone', user.phone)
        user.email = request.data.get('email', user.email)

        if 'image' in request.FILES:
            user.image = request.FILES['image']

        user.save()  

        return Response({
            'Message': 'Profile Updated Successfully',
            'username': user.username,
            'phone': user.phone,
            'email': user.email,
            'image': request.build_absolute_uri(user.image.url) if user.image else None
        })

# ===================================================================================================================