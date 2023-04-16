from django.shortcuts import render
from .forms import AddNewInvestment
from .models import Investment
# Create your views here.
def home(request):
    context= {
        'user': request.user
    }
    return render(request, 'home.html', context)

def addInvestment(request):
    form = AddNewInvestment()
    if request.method == 'POST':
        form = AddNewInvestment(request.POST, request.FILES)
        if form.is_valid():
            new_investment = Investment(
                name=form.cleaned_data['name'],
                img=form.cleaned_data['img'],
                location=form.cleaned_data['location'],
                about=form.cleaned_data['about'],
                price=form.cleaned_data['price'],
                ror=form.cleaned_data['ror'],
                tor=form.cleaned_data['tor'],
            )
            new_investment.save()
            request.user.investment.add(new_investment)
    context = {
        'user': request.user,
        'form': form,
    }
    return render(request, 'addInvestment.html', context)
