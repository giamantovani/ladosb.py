from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compra/', views.compra, name='compra'),
    path('intercambia/', views.intercambia, name='intercambia'),
    path('coleccion/', views.coleccion, name='coleccion'),
    path('', views.lista_discos, name='lista_discos'),
    path('disco/<int:id>/', views.detalle_disco, name='detalle_disco'),
    path('nuevo/', views.nuevo_disco, name='nuevo_disco'),
    path('disco/<int:id>/editar/', views.editar_disco, name='editar_disco'),
    path('disco/<int:id>/eliminar/', views.eliminar_disco, name='eliminar_disco'),
]