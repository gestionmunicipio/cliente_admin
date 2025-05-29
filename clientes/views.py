from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Cliente
from .forms import ClienteForm

from django.contrib.auth.decorators import permission_required

# Listar clientes
@login_required
@permission_required('clientes.view_cliente', raise_exception=True)
def lista_clientes(request):
    # DEBUG: imprime los permisos del usuario
    print(request.user.get_all_permissions())
    
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})

# Agregar cliente
@login_required
@permission_required('clientes.view_cliente', raise_exception=True)
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/formulario.html', {'form': form})

# Editar cliente
@login_required
@permission_required('clientes.view_cliente', raise_exception=True)
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/formulario.html', {'form': form})

# Eliminar cliente
@login_required
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/confirmar_eliminar.html', {'cliente': cliente})

# Login

#def login_view(request):
#    if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            login(request, user)
#            return redirect('lista_clientes')
#    return render(request, 'clientes/login.html')

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_clientes')
        else:
            error = "Usuario o contraseña incorrectos"
    return render(request, 'clientes/login.html', {'error': error})



# Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
