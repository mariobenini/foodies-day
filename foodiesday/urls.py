from django.urls import path
from foodiesday.views import index, search_results, loading_page

urlpatterns = [
	path('',index, name='index'),
  path('search/', search_results, name='search_results'),
  path('loading/', loading_page, name='loading')
]