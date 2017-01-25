from django.db import models, IntegrityError
from django.utils import timezone
import datetime
import string
import random


# Create your models here.
class MiniURL(models.Model):
	longURL = models.URLField(verbose_name= 'url to be shortened')
	code = models.CharField(max_length=10, unique=True, blank=True)
	date = models.DateTimeField(auto_now_add=True, verbose_name = "creation date")
	creator = models.CharField(max_length=80, null=True, blank=True)
	counter = models.IntegerField(default=0)
	NB_CARACTERES = 6 # define the length of the code

	def __str__(self):
		return '[{1}] - {0}'.format(self.longURL, self.code)

	def generer(self, nb_caracteres):
		caracteres = string.ascii_letters + string.digits
		aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
		self.code = ''.join(aleatoire)

	def save(self, *args, **kwargs): # override save function to include a generated code
		if self.pk is None: # this checks if a new instance is already created
			self.generer(self.NB_CARACTERES)

		try:
			super(MiniURL, self).save( *args, **kwargs)
		except IntegrityError: # raised if generated code collides with an existing one
			self.generer(self.NB_CARACTERES)
			super(MiniURL, self).save( *args, **kwargs)


