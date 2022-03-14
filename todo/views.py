from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def singupuser(request):

    return render(request, 'todo/singupuser.html', {'form': UserCreationForm()})