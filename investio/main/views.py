from django.shortcuts import render
from .forms import AddNewInvestment

# Create your views here.
def home(request):
    context= {
        'user': request.user
    }
    return render(request, 'home.html', context)

def addInvestment(request):
    form = AddNewInvestment(request.POST)
    context= {
        'user': request.user,
        'form': form,
    }
    return render(request, 'addInvestment.html', context)
