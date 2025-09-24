from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, AddWishForm
from .models import Wish
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib import messages
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
        user_id = request.user.id
        wishes = Wish.objects.filter(user_id=user_id)
    return render(request, 'wish_list.html', {'wishes': wishes})


def public_wish_list(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    wishes = Wish.objects.filter(user=user)
    return render(request, 'public_wish_list.html', {'wishes': wishes, 'wishlist_owner': user})


@login_required
def add_wish(request):
    if request.method == 'POST':
        form = AddWishForm(request.POST, request.FILES)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.user = request.user
            wish.save()
            return redirect('wish_list')
    else:
        form = AddWishForm()
    return render(request, 'add_wish.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'wish_list')
            return redirect(next_url)
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
    
    return render(request, 'login.html')


def public_wish_list(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    wishes = Wish.objects.filter(user=user)
    return render(request, 'public_wish_list.html', {'wishes': wishes, 'wishlist_owner': user})

@login_required
def confirm_delete(request, wish_id):
    wish = get_object_or_404(Wish, id=wish_id, user=request.user)
    if request.method == 'POST':
        wish.delete()
        return redirect('wish_list')
    return render(request, 'confirm_delete.html', {'wish': wish})


