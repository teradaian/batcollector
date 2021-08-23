from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Bat, Relic
from .forms import FeedingForm

class Home(LoginView):
  template_name = 'home.html'

class BatCreate(CreateView):
  model = Bat
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/bats/'

class BatUpdate(UpdateView):
  model = Bat
  fields = ['description', 'age']

class BatDelete(DeleteView):
  model = Bat
  success_url = '/bats/'

class RelicCreate(CreateView):
  model = Relic
  fields = '__all__'

class RelicList(ListView):
  model = Relic

class RelicDetail(DetailView):
  model = Relic

class RelicUpdate(UpdateView):
  model = Relic
  fields = ['name', 'color']

class RelicDelete(DeleteView):
  model = Relic
  success_url = '/relics/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bats_index(request):
  bats = Bat.objects.all()
  return render(request, 'bats/index.html', { 'bats': bats })

def bat_details(request, bat_id):
  bat = Bat.objects.get(id=bat_id)
  relics_bat_doesnt_have = Relic.objects.exclude(id__in = bat.relics.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'bats/detail.html', { 'bat': bat, 'feeding_form': feeding_form, 'relics': relics_bat_doesnt_have })

def add_feeding(request, bat_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.bat_id = bat_id
    new_feeding.save()
  return redirect('bat_details', bat_id=bat_id)

def assoc_relic(request, bat_id, relic_id):
  Bat.objects.get(id=bat_id).relics.add(relic_id)
  return redirect('bat_details', bat_id=bat_id)
  