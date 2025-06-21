from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Proyecto Django: Sistema de Administración de Clientes
# Estructura ampliada con autenticación de usuarios y funcionalidades CRUD completas

class Direccion(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='direcciones')
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.calle}, {self.ciudad}"

class Cliente(models.Model):
    ESTADOS = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    nombre = models.CharField(max_length=100, verbose_name=_("Nombre"))
    
    rut = models.CharField(max_length=20, unique=True, verbose_name=_("Rut"))
    email = models.EmailField()
    telefono = models.CharField(max_length=20, verbose_name=_("Teléfono"))
    fecha_registro = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, verbose_name=_("Estado"))
    observacion = models.TextField(blank=True, verbose_name=_("Observación"))
    #direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, verbose_name=_("Dirección")) --Ahora el cliente tiene n direcciones

    def __str__(self):
        return self.nombre

class HistorialCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    campo_modificado = models.CharField(max_length=50)
    valor_anterior = models.TextField()
    valor_nuevo = models.TextField()
    