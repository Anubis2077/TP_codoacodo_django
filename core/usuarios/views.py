from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from core.usuarios.forms import RegisterForm
from django.views import View
from .forms import LoginForm
from django.contrib import messages

# Create your views here.



class IndexView(TemplateView):
    template_name = 'index.html'

class HomeView(TemplateView):
    template_name='login1.html'

    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        """para poder enviar mas parametros a mi template"""
        context = super().get_context_data(**kwargs) #variable para recuperar lo que ya tiene el context data
        context['title']= 'Iniciar sesión'
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)
    
class Register_index(View):
    form_class = RegisterForm
    template_name = 'register1.html'
    success_url = reverse_lazy('home')

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                return redirect('register')
            print(form.cleaned_data['email'])
            print(form.cleaned_data['username'])
            print(form.cleaned_data['password1'])
            print(form.cleaned_data['password2'])
            user = form.save()
            login(self.request, user)
            return redirect(self.success_url)
        else:
            print(form.errors)
        context = {'form': form}

        return render(request, self.template_name, context)

        context = {'form': form}
        return render(request, self.template_name, context)

class Login_index(View):
    form_class= LoginForm
    template_name= 'login1.html'
    success_url = reverse_lazy('home')

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(self.success_url)
            print(form.errors.as_text())

        context = {'form': form}
        messages.error(request, 'Se produjo un error al enviar el formulario. Por favor, revise los datos e intente nuevamente.')
        return render(request, self.template_name, context)
            



