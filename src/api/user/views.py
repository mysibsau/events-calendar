from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken as StandartObtainAuthToken
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

from api.user.serializer import AuthTokenSerializer, ProfileSerializer, UserSerializer
from apps.user import models, services


class ObtainAuthToken(StandartObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'confirmed': user.confirmed,
            'name': user.first_name,
            'is_staff': user.is_staff,
            'id': user.id,
        })


obtain_auth_token = ObtainAuthToken.as_view()


class ProfileView(RetrieveModelMixin, GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class UserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    queryset = models.User.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ['username', 'email']

    @action(detail=True)
    def confirmed(self, request, pk):
        services.confirm.confirm_user(pk)
        return super().retrieve(request)

    @action(detail=True)
    def ban(self, request, pk):
        services.confirm.ban_user(pk)
        return super().retrieve(request)