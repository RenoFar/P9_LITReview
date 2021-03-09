from django.shortcuts import render


def index(request):
    return render(request, 'home/home.html')


def registration(request):
    return render(request, 'registration/inscription.html')