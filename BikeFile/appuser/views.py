from django.contrib.auth import get_user_model, login
from knox.models import AuthToken
from knox.settings import knox_settings
from rest_framework import generics, permissions, status
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response
from BikeFile.appuser.serializers import AuthenticateTokenSerializer, CreateUserSerializer

UserModel = get_user_model()


class LoginAPIView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        if 'email' in request.data:
            request.data['username'] = request.data['email']

        serializer = AuthenticateTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        user_data = super(LoginAPIView, self).post(request, format=None).data

        return Response({'email': user_data['user']['email'],
                         'expiry': user_data['expiry'],
                         'token': user_data['token']}, status=status.HTTP_201_CREATED)


class RegisterAPIView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        instance, token = AuthToken.objects.create(serializer.instance, knox_settings.TOKEN_TTL)

        return Response({'email': instance.user.email,
                         'expiry': instance.expiry,
                         'token': token}, status=status.HTTP_201_CREATED, headers=headers)
