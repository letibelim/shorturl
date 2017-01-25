from django import forms
from .models import MiniURL


class MiniURLForm(forms.Form):
	creator = forms.CharField(max_length=80, required=False)
	longURL = forms.URLField(label="Copy and paste your url")
	code = forms.CharField(max_length=10, label = "suggested code, you can customize")

	def clean_code(self):
		code = self.cleaned_data['code']
		if len(MiniURL.objects.filter(code=code)) > 0:
			raise forms.ValidationError("Short url already exists, please modify")
		return code



