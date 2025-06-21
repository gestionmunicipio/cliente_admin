from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.views.i18n import set_language

from .views import exportar_clientes_excel, exportar_clientes_pdf

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('nuevo/', views.agregar_cliente, name='agregar_cliente'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('direccion/<int:cliente_id>/eliminar/<int:direccion_id>/', views.eliminar_direccion, name='eliminar_direccion'),
   
    path('direccion/<int:cliente_id>/', views.guardar_direccion, name='nueva_direccion'),
    path('direccion/<int:cliente_id>/<int:direccion_id>/', views.guardar_direccion, name='editar_direccion'),

    path('direccion/<int:cliente_id>/nueva/', views.agregar_direccion, name='agregar_direccion'),

    path('exportar/excel/', exportar_clientes_excel, name='exportar_excel'),
    path('exportar/pdf/', exportar_clientes_pdf, name='exportar_pdf'),
]

urlpatterns += [
    path('set_language/', set_language, name='set_language'),
]