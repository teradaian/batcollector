from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bat, Relic
from .forms import FeedingForm

class Home(LoginView):
  template_name = 'home.html'

class BatCreate(LoginRequiredMixin, CreateView):
  model = Bat
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/bats/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BatUpdate(LoginRequiredMixin, UpdateView):
  model = Bat
  fields = ['description', 'age']

class BatDelete(LoginRequiredMixin, DeleteView):
  model = Bat
  success_url = '/bats/'

class RelicCreate(LoginRequiredMixin, CreateView):
  model = Relic
  fields = '__all__'

class RelicList(LoginRequiredMixin, ListView):
  model = Relic

class RelicDetail(LoginRequiredMixin, DetailView):
  model = Relic

class RelicUpdate(LoginRequiredMixin, UpdateView):
  model = Relic
  fields = ['name', 'color']

class RelicDelete(LoginRequiredMixin, DeleteView):
  model = Relic
  success_url = '/relics/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def bats_index(request):
  bats = Bat.objects.filter(user=request.user)
  return render(request, 'bats/index.html', { 'bats': bats })

@login_required
def bat_details(request, bat_id):
  bat = Bat.objects.get(id=bat_id)
  relics_bat_doesnt_have = Relic.objects.exclude(id__in = bat.relics.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'bats/detail.html', { 'bat': bat, 'feeding_form': feeding_form, 'relics': relics_bat_doesnt_have })

@login_required
def add_feeding(request, bat_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.bat_id = bat_id
    new_feeding.save()
  return redirect('bat_details', bat_id=bat_id)

@login_required
def assoc_relic(request, bat_id, relic_id):
  Bat.objects.get(id=bat_id).relics.add(relic_id)
  return redirect('bat_details', bat_id=bat_id)
  
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('bats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)