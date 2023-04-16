from django.shortcuts import render
from .models import Investment


# Create your views here.
def home(request):
    investments = list(Investment.objects.all())
    context = {
        'user': request.user,
        'investments': investments,
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'user': request.user,
    }
    return render(request, 'about.html', context)
