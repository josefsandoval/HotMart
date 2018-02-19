from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

from .models import Category, Item

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


class CategoryItemView(generic.ListView):
    model = Category
    template_name = 'shop/categories.html'
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()