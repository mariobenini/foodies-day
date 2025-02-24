from django.shortcuts import render
from django.conf import settings

def index(request):
	context = {
		'GOOGLE_PLACES_API_KEY': settings.GOOGLE_PLACES_API_KEY
	}
	return render(request, 'foodiesday/index.html', context)

