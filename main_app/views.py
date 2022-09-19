from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render (request, 'home.html', {'page_name' : 'Home'})

def about(request):
  return render (request, 'about.html', {'page_name' : 'About'}) 


# Mock Data

class Finch: 
  def __init__(self, name, type, region, age):
    self.name = name 
    self.type = type
    self.region = region
    self.age = age

finches = [ 
  Finch('Nilight', 'House Finch', 'North America and Hawaii', 2),
  Finch('Bianca', 'American Gold Finch', 'Alberta to North Carolina', 3),
  Finch('Rosa', 'European Goldfinch', 'Europe', 8),
]

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches' : finches }) 
