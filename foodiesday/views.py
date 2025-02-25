from django.shortcuts import render, redirect
from django.conf import settings
import google.generativeai as genai
import markdown
from django.utils.safestring import mark_safe
import time


def index(request):
	context = {
		'GOOGLE_PLACES_API_KEY': settings.GOOGLE_PLACES_API_KEY
	}
	return render(request, 'foodiesday/index.html', context)


genai.configure(api_key=settings.GOOGLE_GEMINI_API_KEY)

def ask_gemini_about_city(city):
    prompt = f"Generate a one-day travel guide for {city}. The guide should include a structured itinerary from morning to night, with recommended restaurants and nearby attractions. Make sure all recommended places are well-rated and located close to each other for a smooth itinerary. If possible, include links to sources where people can find more details. Provide alternative recommendations in case travelers have extra time. Keep the descriptions engaging and informative. The format should be as follows: 1)Morning: Breakfast at [Restaurant Name] - [Short description]; Visit [Attraction Name] - [Short description]. 2) Mid-Morning: Explore [Location Name] - [Short description]. 3)Lunch: Lunch at [Restaurant Name] - [Short description]. 4) Afternoon: Visit [Attraction Name] - [Short description]; Relax at [Park or Location Name] - [Short description]. 5) Evening: Dinner at [Restaurant Name] - [Short description]. 6) Night: Drinks at [Bar or Lounge Name] - [Short description]."
    
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


def search_results(request):
  city = request.GET.get('city', '')
  if city:
    response = ask_gemini_about_city(city)
    response = mark_safe(markdown.markdown(response))
  else:
    response = 'Please, select a city.'
  return render(request, 'foodiesday/search_results.html', {'response': response})


def loading_page(request):
    city = request.GET.get('city', '')

    if not city:
        return redirect('index')

    return render(request, 'foodiesday/loading.html', {'city': city})