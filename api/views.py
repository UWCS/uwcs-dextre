from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication
from oauth2_provider.contrib.rest_framework.permissions import TokenHasScope
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_403_FORBIDDEN,
)
from rest_framework.views import APIView

from accounts.models import CompsocUser
from events.models import EventPage, EventSignup
from .serializers import (
    DiscordUserSerialiser,
    EventSerialiser,
    EventSignupSerialiser,
    ProfileSerialiser,
    RolesProfileSerialiser,
)


class LanAppProfileView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["lanapp"]

    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse(
                {"detail": "cannot perform that action on an unauthenticated user"},
                status=HTTP_403_FORBIDDEN,
            )
        user = request.user
        compsoc_user = CompsocUser.objects.get(user_id=user.id)
        serializer = ProfileSerialiser(compsoc_user)

        return JsonResponse(serializer.data)


class ProfileView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["profile"]

    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse(
                {"detail": "cannot perform that action on an unauthenticated user"},
                status=HTTP_403_FORBIDDEN,
            )
        user = request.user
        compsoc_user = CompsocUser.objects.get(user_id=user.id)
        serializer = ProfileSerialiser(compsoc_user)

        return JsonResponse(serializer.data)


class RolesProfileView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["roles"]

    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse(
                {"detail": "cannot perform that action on an unauthenticated user"},
                status=HTTP_403_FORBIDDEN,
            )
        user = request.user
        compsoc_user = CompsocUser.objects.get(user_id=user.id)
        serializer = RolesProfileSerialiser(compsoc_user)

        return JsonResponse(serializer.data)


class MemberDiscordInfoApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, uni_id):
        user = get_object_or_404(get_user_model(), username=uni_id)
        compsoc_user = CompsocUser.objects.get(user_id=user.id)
        serializer = DiscordUserSerialiser(compsoc_user)

        return JsonResponse(serializer.data)


class EventSignupView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["event"]

    def post(self, request):
        if not request.data.get("event_id"):
            return JsonResponse(
                {"detail": "event_id field is required but wasn't found"},
                status=HTTP_400_BAD_REQUEST,
            )

        data = {
            "event": request.data.get("event_id"),
            "member": request.user.id,
            "comment": request.data.get("comment"),
        }

        serialiser = EventSignupSerialiser(data=data)
        if serialiser.is_valid():
            serialiser.save()
        else:
            return JsonResponse(serialiser.errors, status=HTTP_400_BAD_REQUEST)

        return JsonResponse(serialiser.data, status=HTTP_201_CREATED)


class EventDeregisterView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ["event"]

    def get(self, request, event_id):
        signup = get_object_or_404(EventSignup, event=event_id, member=request.user.id)
        signup.delete()

        return JsonResponse({"detail": "signup deleted"}, status=HTTP_200_OK)


class EventListView(ListAPIView):
    queryset = (
        EventPage.objects.live().filter(finish__gte=timezone.now()).order_by("start")
    )
    serializer_class = EventSerialiser
