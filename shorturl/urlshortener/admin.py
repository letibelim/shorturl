from django.contrib import admin
from .models import MiniURL

# Register your models here.
class MiniURLAdmin(admin.ModelAdmin):
	list_display = (
		'longURL',
		'code',
		'date',
		'creator',
		'counter',
		)

	list_filter = (
		'creator',
		)

	ordering = ('date',)

	search_field = (
		'longURL',
		'creator'
		)


admin.site.register(MiniURL, MiniURLAdmin)