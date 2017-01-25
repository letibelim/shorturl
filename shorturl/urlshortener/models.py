from django.db import models, IntegrityError
from django.utils import timezone
import datetime


# Create your models here.
class MiniURL(models.Model):
	longURL = models.URLField(verbose_name= 'url to be shortened')
	code = models.CharField(max_length=10, unique=True,)
	date = models.DateTimeField(auto_now_add=True, verbose_name = "creation date")
	creator = models.CharField(max_length=80, null=True, blank=True)
	counter = models.IntegerField(default=0)
	NB_CARACTERES = 6 # define the length of the code

	def __str__(self):
		return '[{1}] - {0}'.format(self.longURL, self.code)



