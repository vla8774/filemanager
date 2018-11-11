
# Django
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin, LoginAjaxMixin
# Project

from .forms import CustomUserCreationForm, CustomAuthenticationForm, CustomUserChangeForm

from .forms import CustomUserCreationForm



class SignUp(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'account/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('post_list')


class CustomLoginView(LoginAjaxMixin, SuccessMessageMixin, LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'account/login.html'
    success_message = 'Success: You were successfully logged in.'
    #success_url = reverse_lazy('post_list')


class Change(generic.CreateView):
    form_class = CustomUserChangeForm
    template_name = 'account/change.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('post_list')

