from django.shortcuts import render


def subs(request):
    return render(request, 'subs/abonnements.html')