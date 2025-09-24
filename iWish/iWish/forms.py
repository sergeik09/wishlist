from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import CustomUser, Wish

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

class AddWishForm(ModelForm):
    class Meta:
        model = Wish
        fields = ('title', 'desc', 'link', 'image')

