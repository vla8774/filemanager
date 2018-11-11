from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'photo')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'photo')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']