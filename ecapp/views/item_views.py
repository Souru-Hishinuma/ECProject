from django.shortcuts import render
from django.views.generic import ListView
from ecapp.models import Item

class IndexListView(ListView):
    model = Item
    template_name = 'pages/index.html'