from django.urls import path
from foodiesday.views import index

urlpatterns = [
	path('',index)
]