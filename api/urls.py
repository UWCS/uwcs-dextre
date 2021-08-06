from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # url('^events/$', views.EventListView.as_view(), name='events_list_view'),
    # url('^events/signup/$', views.EventSignupView.as_view(), name='events_signup_view'),
    # url('^events/deregister/(?P<event_id>[0-9]+)/$', views.EventDeregisterView.as_view(), name='events_deregister_view'),
    url('^me$', views.LanAppProfileView.as_view(), name='lanapp_profile_view'),
    url('^user/(?P<uni_id>[0-9]+)/$', views.MemberDiscordInfoApiView.as_view(), name='discord_user_view'),
    path('profile/', views.ProfileView.as_view(), name='profile_view'),
    path('profile/roles/', views.RolesProfileView.as_view(), name='roles_profile_view'),
]
