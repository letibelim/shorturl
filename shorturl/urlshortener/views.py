from django.shortcuts import render,redirect, get_object_or_404
from .models import MiniURL, IntegrityError
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

def generer(nb_caracteres):
	caracteres = string.ascii_letters + string.digits
	aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
	return ''.join(aleatoire)

def urlform(request):
	"""display the form"""
	correctness = False

	if request.method == 'POST':
		form = MiniURLForm(request.POST)
	else: form = MiniURLForm(initial={'code': generer(6)})

	if form.is_valid():
	
		url = MiniURL(
			longURL = form.cleaned_data['longURL'],
			creator = form.cleaned_data['creator'],
			code = form.cleaned_data['code']
			)

		url.save()
		url.code = ''
		correctness = True

	return render(request, 'urlshortener/urlform.html', locals())



