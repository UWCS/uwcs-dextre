from django import forms
from .validators import validate_file_size

SEND_TO_OPTIONS = [
    ('exec', 'All Exec'),
    ('preswelfare', 'President, Welfare & Women\'s Officer'),
    ('president', 'President'),
    ('secretary', 'Secretary'),
    ('treasurer', 'Treasurer'),
    ('academic-coordinator', 'Academic Coordinator'),
    ('gaming-coordinator', 'Gaming Coordinator'),
    ('tech', 'Tech Officer'),
    ('womens-officer', 'Women\'s Officer'),
    ('socials', 'Social Secretary'),
    ('welfare', 'Welfare Officer'),
]

class ReportForm(forms.Form):
    send_to = forms.CharField(widget=forms.Select(choices=SEND_TO_OPTIONS))
    message = forms.CharField(widget=forms.Textarea, required=True)
    ev_file = forms.FileField(required=False, validators=[validate_file_size])