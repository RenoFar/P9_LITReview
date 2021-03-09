from django.shortcuts import render


def flux(request):
    return render(request, 'flux/flux.html')


def critic(request):
    return render(request, 'critic/critique.html')


def posts(request):
    return render(request, 'posts/posts.html')


def subs(request):
    return render(request, 'subs/abonnements.html')


def ticket(request):
    return render(request, 'ticket/ticket.html')
    

def comment(request):
    return render(request, 'comment/commentaire.html')