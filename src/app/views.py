from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import *

import datetime
import base64
import requests

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    
def index(request):
    p = Post(date=datetime.datetime.now(), photo=random_picture())
    p.save(force_insert=True)
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts': posts})


def pizzas(request):
    Pizza(name="Brutalis", description="Betegmódon csípős pizza, fullba vedd meg!").save()
    Pizza(name="Extra finom", description="Nagyon finom pizza, belekóstolsz, vége. Még a tányért is...").save()
    Pizza(name="SAMPLE TEXT", description="SAMPLE PIZZA").save()
    pizzas = Pizza.objects.all().order_by('-name')
    return render(request, 'pizza/pizzexample.html', {'pizzas': pizzas})


def random_picture():
    url = "https://source.unsplash.com/random/400x400"
    response = requests.get(url, stream=True)
    encoded_string = base64.b64encode(response.content)
    del response
    return encoded_string.decode('ascii')
