from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer
from .models import UserModel


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            if user.role == "ceo":
                user.is_superuser = True
                user.is_staff = True
                user.save()

            return Response({
                "success": True,
                "message": "Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tkazildi!",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "role": user.role,
                    "company": user.company,
                    "location": user.location,
                    "phone_number": user.phone_number,
                }
            }, status=status.HTTP_201_CREATED)
        
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)
            response = {
                'success': True,
                "message": "Muvaffaqiyatli tizimga kirildi!",
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    "id": user.id,
                    "username": user.username,
                    "role": user.role,
                    "company": user.company,
                    "location": user.location,
                    "phone_number": user.phone_number,
                }
            }
            return Response(response, status=status.HTTP_200_OK)

        response = {
            "success": False,
            "message": "Username yoki parol xato!",
            "errors": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"success": False, "message": "Token taqdim etilmadi!"},
                                status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"success": True, "message": "Siz tizimdan chiqdingiz!"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"success": False, "message": "Xato yuz berdi!", "error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class PermissionOpen(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.role == "ceo":
            return Response({"success": True, "message": "Siz Boshqaruvchi (CEO) sifatida barcha tizimga kirdingiz!"}, status=status.HTTP_200_OK)
        elif user.role == "mentor":
            return Response({"success": True, "message": "Siz Mentor sifatida admin panelga kira olasiz!"}, status=status.HTTP_200_OK)
        elif user.role == "admin":
            return Response({"success": True, "message": "Siz Administrator sifatida tizimga kirdingiz!"}, status=status.HTTP_200_OK)
        elif user.role == "student":
            return Response({"success": True, "message": "Siz O'quvchi sifatida tizimga kirdingiz!"}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False, "message": "Sizga ruxsat berilmagan!"}, status=status.HTTP_403_FORBIDDEN)