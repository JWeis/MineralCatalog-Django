from django.shortcuts import render
from .models import Mineral

# Create your views here.


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/home.html', {'minerals':minerals})


def mineral_detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'minerals/detail.html', {'mineral':mineral})