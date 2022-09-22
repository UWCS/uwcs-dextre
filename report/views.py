from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.views import View
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from .forms import ReportForm


class ReportView(FormView):
    form_class = ReportForm
    template_name = "report/report_form.html"
    success_url = "success/"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            from_email = "UWCS <noreply@uwcs.co.uk>"
            to_email = form.cleaned_data["send_to"]

            if to_email == "preswelfare":
                to_list = [
                    "president@uwcs.co.uk",
                    "welfare@uwcs.co.uk",
                    "inclusivity@uwcs.co.uk",
                ]
            else:
                to_email = to_email + "@uwcs.co.uk"
                to_list = [to_email]
            email_context = {
                "subject": "New anonymous report received",
                "message": form.cleaned_data["message"],
            }

            email_html = render_to_string("report/report_received.html", email_context)
            email_text = render_to_string("report/report_received.txt", email_context)

            email = EmailMultiAlternatives(
                email_context["subject"], email_text, from_email, to=to_list
            )
            email.attach_alternative(email_html, "text/html")
            if request.FILES:
                ev_file = request.FILES["ev_file"]
                email.attach(ev_file.name, ev_file.read(), ev_file.content_type)

            email.send()
            return HttpResponseRedirect("success/")
        return render(request, self.template_name, {"form": form})


class SuccessView(View):
    template_name = "report/report_success.html"

    def get(self, request):
        return render(request, self.template_name)
