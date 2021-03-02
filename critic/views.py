from django.shortcuts import render


def critic(request):
    return render(request, 'critic/critique.html')