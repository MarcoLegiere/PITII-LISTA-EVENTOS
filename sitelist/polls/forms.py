from django import forms

from .models import Funcionario

class ConfirmFunc(forms.Form):
    meeting_id = forms.ModelChoiceField(queryset=Funcionario.objects.all())

