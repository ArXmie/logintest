from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'registration/login.html')

@login_required
def personal(request):
    return render(request, 'personal.html')