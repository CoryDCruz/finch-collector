from django.shortcuts import render, redirect
from .models import Finch
from .models import Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import FeedingForm

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
  feeding_form = FeedingForm()
  toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))

  return render(request, 'finches/detail.html', 
  { 
    'finch': finch, 
    'page_name' : 'Details',
    'feeding_form' : feeding_form,
    'toys': toys_finch_doesnt_have,
  })

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)

  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('details', finch_id)

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  # Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('details', finch_id)


class FinchCreate(CreateView):
  model = Finch
  fields = ('age', 'type', 'region')

class FinchUpdate(UpdateView):
  model = Finch
  fields = ('age', 'type', 'region')

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView): 
  model = Toy
  context_object_name = 'toys'

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = {'name', 'color'}

class ToyDelete(DeleteView):
  model = Toy 
  success_url = '/toys/'
