from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .forms import RegisterUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginUserForm
from django.contrib.auth import logout, login




class RegisterFormView(FormView):
    form_class = RegisterUserForm
    template_name = 'login/register.html'
    success_url = reverse_lazy('home')

    # def form_valid(self, form):
    #     form.save()
    #     return super (RegisterFormView, self). form_valid(form)

    # def form_invalid(self, form):
    #     return super (RegisterFormView, self). form_invalid(form)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login/login.html'
    success_url = reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
   
