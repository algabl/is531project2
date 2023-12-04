# views.py

from django.shortcuts import render
from .models import Mousepad

def home(request):
    mousepad_list = Mousepad.objects.all()
    return render(request, 'home.html', {'mousepad_list': mousepad_list})