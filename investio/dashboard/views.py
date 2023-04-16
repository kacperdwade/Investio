from django.shortcuts import render


# Create your views here.
def home(request):
    # investments = list(Investment.objects.all())
    context = {
        'user': request.user,
        # 'investments': investments,
    }
    return render(request, 'dashboard_home.html', context)
