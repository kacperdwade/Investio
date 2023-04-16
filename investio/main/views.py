from django.shortcuts import render, redirect
from .forms import AddNewInvestment
from .models import Investment


# Create your views here.
def home(request):
    investments = list(Investment.objects.all())
    context = {
        'user': request.user,
        'investments': investments,
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
            return redirect('main:home')
    context = {
        'user': request.user,
        'form': form,
    }
    return render(request, 'add_investment.html', context)


def userInvestments(request):
    investments = list(request.user.investment.all())
    context = {
        'user': request.user,
        'investments': investments,
    }
    return render(request, 'user_investments.html', context)

def about(request):
    context = {
        'user': request.user,
    }
    return render(request, 'about.html', context)
