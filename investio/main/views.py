from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddNewInvestment
from .models import Investment, Image


# Create your views here.
def home(request):
    parameters = request.GET
    print(len(parameters))
    if len(parameters) != 0:
        location = request.GET.get('location').lower()
        print(location)
        if request.method == 'GET':
            investments = list(Investment.objects.filter(location=location))
            print(investments)
    else:
        investments = list(Investment.objects.all())
        test = [(i, Image.objects.filter(investment=i).first()) for i in list(Investment.objects.all())]
        print(test)
    context = {
        'user': request.user,
        'investments': test,
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'user': request.user,
    }
    return render(request, 'about.html', context)

def add_investment(request):
    form = AddNewInvestment()
    if request.method == 'POST':
        form = AddNewInvestment(request.POST, request.FILES)
        if form.is_valid():
            new_investment = Investment(
                name=form.cleaned_data['name'],
                #img=form.cleaned_data['img'],
                location=form.cleaned_data['location'],
                about=form.cleaned_data['about'],
                price=form.cleaned_data['price'],
                ror=form.cleaned_data['ror'],
                tor=form.cleaned_data['tor'],
            )
            new_investment.save()
            request.user.investment.add(new_investment)
            images = request.FILES.getlist('img')
            for image in images:
                photo = Image.objects.create(
                    investment=new_investment,
                    img=image
                )
            return redirect('../')
    context = {
        'user': request.user,
        'form': form,
    }
    return render(request, 'add_investment.html', context)


def user_investments(request):
    investments = list(request.user.investment.all())
    context = {
        'user': request.user,
        'investments': investments,
    }
    return render(request, 'user_investments.html', context)

def investment_detail_view(request, id_):
    investment = get_object_or_404(Investment, id=id_)
    # investments = list(Investment.objects.all())
    context = {
        'user': request.user,
        'investment': investment,
    }
    return render(request, 'investment_detail.html', context)
