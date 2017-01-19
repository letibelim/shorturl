from django.db import models
from django.utils import timezone
import datetime
import string

# Create your models here.
class MiniURL(models.Model):
	longURL = models.URLField(unique=True, verbose_name= 'url to be shortened')
	code = models.CharField(max_length=10, unique=True)
	date = models.DateTimeField(auto_now_add=True, verbose_name = "creation date")
	creator = models.CharField(max_length=80, null=True)
	counter = models.IntegerField(default=0)

	def __str__(self):
		return '[{1}] - {0}'.format(self.longURL, self.code)