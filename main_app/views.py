from django.shortcuts import render


class Bat: 
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

bats = [
  Bat('Lolo', 'tabby', 'Kinda rude.', 3),
  Bat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Bat('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Bat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bats_index(request):
  return render(request, 'bats/index.html', { 'bats': bats })