from django.shortcuts import render
from urlshortener import MiniURL
from .forms import MiniURLForm

# Create your views here.

def all_redirections(request):
	"""display all URL et their shortened code"""
	urls = MiniURL.objects.all()
	render(request, 'urlshortener/allurl.html', {'list_of_urls': urls})

def redirection(request, codesent):
	""" redirect the shortened url to the original one"""
	
	url = MiniURL.objects.get(code=codesent)
	redirect (url.longURL)

def urlform(request):
	"""display the form"""
	form = MiniURLForm(request.POST or None)

	if form.is_valid():
		longURL = form.cleaned_data['longURL']
		creator = form.cleaned_data['creator']

	

