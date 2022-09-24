from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import FeedingForm
from .models import Finch, Toy


# Create your views here.
def home(request):
  return render (request, 'home.html', {'page_name' : 'Home'})

def about(request):
  return render (request, 'about.html', {'page_name' : 'About'}) 

def finches_index(request):
  finches = Finch.objects.filter(user=request.user)
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

def signup(request):
  form = UserCreationForm()
  error_message = ''

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'invalid credentials'
  
  context = {'form' : form, 'error_messages' : error_message}
  return render(request, 'registration/signup.html', context)

class FinchCreate(CreateView):
  model = Finch
  fields = ('name', 'age', 'type', 'region')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class FinchUpdate(UpdateView):
  model = Finch
  fields = ('name','age', 'type', 'region')

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
