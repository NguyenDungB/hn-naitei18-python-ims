from django.shortcuts import render
from django.views import generic
from myalbums.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
def index(request):
	return render(request, 'index.html')

