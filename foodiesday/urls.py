from django.urls import path
from foodiesday.views import index
from foodiesday.views import search_results

urlpatterns = [
	path('',index, name='index'),
  path('search/', search_results, name='search_results')
]