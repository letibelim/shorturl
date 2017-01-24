from django.shortcuts import render,redirect, get_object_or_404
from .models import MiniURL
from .forms import MiniURLForm

import random
import string

# Create your views here.


def test(request):

	return render(request, 'urlshortener/test.html')

def all_redirections(request):
	"""display all URL and their shortened code"""
	urls = MiniURL.objects.all()
	return render(
		request, 
		'urlshortener/allurl.html', 
		{'list_of_urls': urls}
		)

def redirection(request, code):
	""" redirect the shortened url to the original one"""
	mini = get_object_or_404(MiniURL, code=code)
	mini.counter += 1
	mini.save()
	return redirect(mini.longURL, permanent=True)


def urlform(request):
	"""display the form"""

	form = MiniURLForm(request.POST or None)

	if form.is_valid():
		
		url = MiniURL(
			longURL = form.cleaned_data['longURL'],
			creator = form.cleaned_data['creator'],
			)

		url.save()
		correctness = True

	return render(request, 'urlshortener/urlform.html', locals())



