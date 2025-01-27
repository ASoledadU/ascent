from django import forms
from initiative.models import Initiative
from django.utils import timezone
from django.contrib.auth.models import User


class InitiativeForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()


class StatusReportForm(forms.Form):
    content = forms.CharField()


class InitiativeEditForm(forms.ModelForm):
    class Meta:
        model = Initiative
        fields = ["team_leader", "title", "description"]
        widgets = {"title": forms.TextInput()}
