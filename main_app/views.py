from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat, Feeding
from .forms import FeedingForm

from django.views.generic import CreateView, UpdateView, DeleteView


# Create your views here.

# define home view
def home(request):
    return render(request, 'home.html');

# about

def about(request):
    return render(request, 'about.html');

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})


def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})

# class CatDetails(DetailView):
#     model = Cat
#     template_name = 'cats/detail.html'
   

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats/'

class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']


class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

# Feedings 

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)    


def delete_feeding(request, feeding_id):
    feeding = Feeding.objects.get(id=feeding_id)
    cat_id = feeding.cat.id 
    feeding.delete()
    return redirect('cat-detail', cat_id=cat_id)













    # Fake DataBase
# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name 
#         self.breed = breed 
#         self.description = description
#         self.age = age 
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]
