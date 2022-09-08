from django import forms
from .models import sitelist

class ConfirmUserForm(forms.Form):
    confimUser = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
