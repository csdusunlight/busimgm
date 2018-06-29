from .models import User
from django.contrib.auth.forms import UserCreationForm
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('uid','uname','uqq')

from django.contrib.auth.forms import UserChangeForm
class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
