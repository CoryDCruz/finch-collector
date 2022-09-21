from django.shortcuts import render
from django.http import HttpResponse
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
  return render (request, 'home.html', {'page_name' : 'Home'})

def about(request):
  return render (request, 'about.html', {'page_name' : 'About'}) 

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches' : finches, 'page_name': 'Finches' }) 

def finch_details(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/details.html', { 'finch': finch, 'page_name' : 'Details'})

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ('age', 'type', 'region')

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

