from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Bat

class BatCreate(CreateView):
  model = Bat
  fields = '__all__'



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bats_index(request):
  bats = Bat.objects.all()
  return render(request, 'bats/index.html', { 'bats': bats })

def bat_details(request, bat_id):
  bat = Bat.objects.get(id=bat_id)
  return render(request, 'bats/detail.html', { 'bat': bat })