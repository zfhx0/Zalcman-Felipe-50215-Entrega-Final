from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

# Create your views here.
@login_required
def buscar(request):
    if request.methon == "POST":
        buscar = request.POST['buscar']
        return render(request, "aplicacion/templates/aplicacion/users_search.html", {'buscar':buscar})
    else:
        return render(request, "aplicacion/templates/aplicacion/users_search.html")

def home(request):
    return render(request, "aplicacion/index.html") 

@login_required
def users_search(request):
    return render(request, "users_search.html") 

@login_required
def user_settings(request):
    return render(request, "aplicacion/user_settings.html") 

#users
class UserList(ListView, LoginRequiredMixin):
    model = User
    template_name = "aplicacion/User_list.html"
    context_object_name = 'User_list'

class UserCreate(CreateView, LoginRequiredMixin):
    model = User
    fields = ["nombre", "apellido", "email", "dni"]
    success_url = reverse_lazy("users")

class UserDelete(DeleteView, LoginRequiredMixin):
    model = User
    success_url = reverse_lazy("users")

class UserUpdate(UpdateView, LoginRequiredMixin):
    model = User
    fields = ["nombre", "apellido", "email", "dni"]
    success_url = reverse_lazy("users")

#cheques
class ChequesList(ListView, LoginRequiredMixin):
    model = Cheques
    template_name = "aplicacion/Cheques_list.html"
    context_object_name = 'Cheques_list'

class ChequesCreate(CreateView, LoginRequiredMixin):
    model = Cheques
    fields = ["banco", "fecha", "monto", "numero", "perteneciente"]
    success_url = reverse_lazy("cheques")

class ChequesDelete(DeleteView, LoginRequiredMixin):
    model = Cheques
    success_url = reverse_lazy("cheques")

class ChequesUpdate(UpdateView, LoginRequiredMixin):
    model = Cheques
    fields = ["banco", "fecha", "monto", "numero", "perteneciente"]
    success_url = reverse_lazy("cheques")

#clientes
class ClienteList(ListView, LoginRequiredMixin):
    model = Cliente
    template_name = "aplicacion/Clientes_list.html"
    context_object_name = 'Clientes_list'

class ClienteCreate(CreateView, LoginRequiredMixin):
    model = Cliente
    fields = ["nombre", "apellido", "email", "dni", "empresa"]
    success_url = reverse_lazy("clientes")

class ClienteDelete(DeleteView, LoginRequiredMixin):
    model = Cliente
    success_url = reverse_lazy("clientes")

class ClienteUpdate(UpdateView, LoginRequiredMixin):
    model = Cliente
    fields = ["nombre", "apellido", "email", "dni", "empresa"]
    success_url = reverse_lazy("clientes")

#pagos
class PagoList(ListView, LoginRequiredMixin):
    model = PagoPendiente
    template_name = "aplicacion/pagos_list.html"
    context_object_name = 'pagos_list'

class PagoCreate(CreateView, LoginRequiredMixin):
    model = PagoPendiente
    fields = ["deudor", "vencimiento", "monto", "numero", "perteneciente"]
    success_url = reverse_lazy("pagos")

class PagoDelete(DeleteView, LoginRequiredMixin):
    model = PagoPendiente
    success_url = reverse_lazy("pagos")

class PagoUpdate(UpdateView, LoginRequiredMixin):
    model = PagoPendiente
    fields = ["deudor", "vencimiento", "monto", "numero", "perteneciente"]
    success_url = reverse_lazy("pagos")

#login
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        form = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":form})

#logout
@login_required
def logout_request(request):
    logout(request)
    return redirect(reverse_lazy('home'))

#register
@login_required
def registration_request(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid() :
            usuario = miForm.cleaned_data.get("username")
            password = miForm.cleaned_data.get("password2")
            miForm.save()
            user = authenticate(request, username=usuario, password=password)
            login(request, user)
            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('register'))
    else:
        miForm = RegistroForm()
        return render(request, "aplicacion/register.html", {'form': miForm})