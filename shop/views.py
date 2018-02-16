from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'shop/home.html')
    #return HttpResponse('Hello There')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shop')

    else:
        form = UserCreationForm()
        context = {'form': form}
    return render(request, 'shop/registration_form.html', context)