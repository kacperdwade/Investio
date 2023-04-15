from django.shortcuts import render
from .forms import AddNewInvestment
from models import Investment
# Create your views here.
def home(request):
    context= {
        'user': request.user
    }
    return render(request, 'home.html', context)

def addInvestment(request):
    if request.method == 'POST':
        form = AddNewInvestment(request.POST)
        if form.is_valid():
            new_investment = Investment(
                name=form.name,
                img=form.img,
                location=form.location,
                about=form.about,
                price=form.price,
                ror=form.ror,
                tor=form.tor,
            )

    context = {
        'user': request.user,
        'form': form,
    }
    return render(request, 'addInvestment.html', context)
