from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from .models import UserModel


class RegisterSerializer(serializers.ModelSerializer):
    """Yangi foydalanuvchini ro'yxatdan o'tkazish uchun serializer"""
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password', 'role', 'company', 'location', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data.get('role', 'user'),
            company=validated_data.get('company', ''),
            location=validated_data.get('location', ''),
            phone_number=validated_data.get('phone_number', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, max_length=150)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username and not email:
            raise serializers.ValidationError("Username yoki email kiritilishi kerak.")

        user = None
        if username:
            user = UserModel.objects.filter(username=username).first()
        elif email:
            user = UserModel.objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError("Foydalanuvchi topilmadi.")

        if not user.check_password(password):
            raise serializers.ValidationError("Username yoki parol noto‘g‘ri.")

        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi faollashtirilmagan.")

        data["user"] = user
        return data


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {
        'bad_token': 'Token not valid or expired',
        'no_token': 'Token is missing'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
