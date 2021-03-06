from api.events import permissions, serializers
from apps.events import models
from apps.events.services import verification
from apps.user.models import UserRole
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class EventViewSet(ModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.all()
    permission_classes = [permissions.IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("id", "name")

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_authenticated:
            return queryset.filter(
                verified=True,
                coverage_participants_fact__isnull=True,  # TODO: заменить на статус мероприятия
                important_dates__isnull=False,
            )
        if self.request.user.role == UserRole.author:
            return queryset.filter(author=self.request.user)
        return queryset


class DirectionViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = serializers.DirectionSerializer
    queryset = models.Direction.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["id", "name"]


class LevelViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = serializers.LevelSerializer
    queryset = models.Level.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["id", "name"]


class RoleViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = serializers.RoleSerializer
    queryset = models.Role.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["id", "name"]


class FormatViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = serializers.FormatSerializer
    queryset = models.Format.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["id", "name"]


class OrganizationViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = serializers.OrganizationSerializer
    queryset = models.Organization.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ["id", "name"]


class VerifyEvent(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, event_id, *args, **kwargs):
        verification.verify_event(event_id, request.user)

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, event_id, *args, **kwargs):
        verification.cancel_event_verification(event_id)

        return Response(status=status.HTTP_200_OK)


class CommentViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, permissions.IsOwnerCommentOrReadOnly]
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        serializer.validated_data["author"] = self.request.user
        serializer.save()

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)
