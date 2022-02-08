from django.core.management.base import BaseCommand
from django.conf import settings

from django.template.defaultfilters import title

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

import requests

# Use the C ElementTree implementation where possible
try:
    from xml.etree.cElementTree import ElementTree, fromstring
except ImportError:
    from xml.etree.ElementTree import ElementTree, fromstring

API_PREFIX = "https://www.warwicksu.com/membershipapi/listMembers/"


def send_signup_mail(user, password):
    email_context = {
        "title": "Welcome to the University of Warwick Computing Society",
        "first_name": user.first_name,
        "username": user.username,
        "password": password,
    }
    email_html = render_to_string("accounts/signup_mail.html", email_context)
    email_text = render_to_string("accounts/signup_mail.txt", email_context)

    email = EmailMultiAlternatives(
        email_context["title"],
        email_text,
        "UWCS Exec <noreply@uwcs.co.uk>",
        to=[user.email],
    )
    email.attach_alternative(email_html, "text/html")
    email.send()


class Command(BaseCommand):
    def handle(self, *args, **options):
        members_xml = requests.get(
            "{prefix}{key}/".format(prefix=API_PREFIX, key=settings.UNION_API_KEY)
        )
        members_root = fromstring(members_xml.text.encode("utf-8"))
        active_members = []

        # Add any new members
        for member in members_root:
            try:
                if member.find("UniqueID").text:
                    current_member = User.objects.get(
                        username=member.find("UniqueID").text
                    )
                    active_members.append(current_member.id)
            except User.DoesNotExist:
                # Create the user and then email their password to them
                password = User.objects.make_random_password()
                new_user = User.objects.create_user(
                    username=member.find("UniqueID").text,
                    email=member.find("EmailAddress").text,
                    password=password,
                )
                new_user.first_name = title(member.find("FirstName").text)
                new_user.last_name = title(member.find("LastName").text)
                new_user.save()
                send_signup_mail(new_user, password)
                active_members.append(new_user.id)

        # Handle special cases with Ex-exec, exec and staff/superuser status
        for member in User.objects.all():
            if member.groups.filter(
                name__in=["Ex-exec", "Exec", "Active Alumni"]
            ).exists():
                if member not in active_members:
                    active_members.append(member.id)
            elif member.is_staff or member.is_superuser:
                if member not in active_members:
                    active_members.append(member.id)

        # Ensure all accounts that are to be activate are so
        activated = User.objects.filter(id__in=active_members).all()
        activated.update(is_active=True)

        # Deactivate old accounts
        deactivated = User.objects.exclude(id__in=active_members).all()
        deactivated.update(is_active=False)
