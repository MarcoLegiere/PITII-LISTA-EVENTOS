from django import forms

from .models import Funcionario

class ConfirmFunc(forms.Form):
    meeting = forms.ModelChoiceField(queryset=Funcionario.objects.all())

