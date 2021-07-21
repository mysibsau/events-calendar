from rest_framework import serializers

from . import models


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = ('id', 'name', 'start_date', 'stop_date')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'


class EventDetailSerializer(serializers.ModelSerializer):
    responsible = serializers.StringRelatedField(source='responsible.first_name', read_only=True)
    verified = serializers.StringRelatedField(source='verified.first_name', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    can_edit = serializers.BooleanField(read_only=True, label='Может ли данный пользователь редактировать мероприятие')

    class Meta:
        model = models.Event
        fields = '__all__'


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Direction
        fields = '__all__'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Level
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Format
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = '__all__'
