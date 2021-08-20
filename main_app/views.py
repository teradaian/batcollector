from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bat

class BatCreate(CreateView):
  model = Bat
  fields = '__all__'
  success_url = '/bats/'

class BatUpdate(UpdateView):
  model = Bat
  fields = ['description', 'age']

class BatDelete(DeleteView):
  model = Bat
  success_url = '/bats/'

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