from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, AddWishForm
from .models import Wish


@login_required
def home(request):
    pass


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


@login_required
def wish_list(request):
    if request.method == 'GET':
        wishes = Wish.objects.all()


def add_wish(request):
    if request.method == 'POST':
        form = AddWishForm(request.POST)
        if form.is_valid():
            wish = form.save()
        else:
            form = AddWishForm()
    return render(request, 'add_wish.html', {'form': form})

def login(request):
    pass

def public_wish_list(request):
    pass

def confirm_delete(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    pass