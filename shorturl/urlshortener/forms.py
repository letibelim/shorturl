from django import forms
from .models import MiniURL

class MiniURLForm(forms.Form):
	creator = forms.CharField(max_length=80, required=False)
	longURL = forms.URLField(label="Copy and paste your url")
	#code = forms.CharField(max_length=10, initial= generer(6), label = "suggested code, you can customize")


