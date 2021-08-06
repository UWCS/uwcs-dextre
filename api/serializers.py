from django.contrib.auth.models import User, Group
from rest_framework import serializers

from events.models import EventPage, EventSignup


class DiscordUserSerialiser(serializers.Serializer):
    discord_user = serializers.CharField(read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class GroupSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserGroupSerialiser(serializers.ModelSerializer):
    groups = GroupSerialiser(many=True)

    class Meta:
        model = User
        fields = ['groups', 'is_staff', 'is_superuser']


class RolesProfileSerialiser(serializers.Serializer):
    nickname = serializers.CharField(read_only=True)
    user = UserGroupSerialiser()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class ProfileSerialiser(serializers.Serializer):
    nickname = serializers.CharField(read_only=True)
    user = UserSerialiser()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class EventSignupSerialiser(serializers.ModelSerializer):
    class Meta:
        model = EventSignup
        fields = ('event', 'member', 'signup_created', 'comment')


class EventSerialiser(serializers.ModelSerializer):
    class Meta:
        model = EventPage
        fields = (
            'title', 'id', 'location', 'start', 'finish', 'description', 'cancelled', 'signup_limit', 'signup_open',
            'signup_close', 'signup_freshers_open', 'signup_count')
