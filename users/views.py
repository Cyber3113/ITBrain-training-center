from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from .permissions import IsMentor
from rest_framework.views import APIView
from rest_framework.response import Response



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  



class MentorOnlyView(APIView):
    """
    Bu API faqat mentorlar uchun ishlaydi
    """
    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):
        return Response({"message": f"Salom, {request.user.username}! Siz mentor sifatida tizimdasiz."})
