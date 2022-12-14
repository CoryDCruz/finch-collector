import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import FeedingForm
from .models import Finch, Photo, Toy

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'finch-collector-image-assets'

# Create your views here.
def home(request):
  return render (request, 'home.html', {'page_name' : 'Home'})

def about(request):
  return render (request, 'about.html', {'page_name' : 'About'}) 

@login_required
def finches_index(request):
  finches = Finch.objects.filter(user=request.user)
  return render(request, 'finches/index.html', { 'finches' : finches, 'page_name': 'Finches' }) 

@login_required
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

@login_required
def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)

  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('details', finch_id)

@login_required
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

def add_photo(request, finch_id):
  photo_file = request.FILES.get('photo-file')

  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try: 
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f'{S3_BASE_URL}{BUCKET}/{key}'
      photo = Photo(url=url, finch_id = finch_id)
      photo.save()
    except:
      print('An error occured with uploading to S3')
  
  return redirect('details', finch_id = finch_id)


class FinchCreate(LoginRequiredMixin, CreateView):
  model = Finch
  fields = ('name', 'age', 'type', 'region')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class FinchUpdate(LoginRequiredMixin, UpdateView):
  model = Finch
  fields = ('name','age', 'type', 'region')

class FinchDelete(LoginRequiredMixin, DeleteView):
  model = Finch
  success_url = '/finches/'

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView): 
  model = Toy
  context_object_name = 'toys'

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = {'name', 'color'}

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy 
  success_url = '/toys/'
