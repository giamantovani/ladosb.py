from django.shortcuts import get_object_or_404, redirect, render
from .models import Disco
from .forms import DiscoForm


# Create your views here.
def index(request):
    discos = Disco.objects.all()
    return render(request, 'index.html', {'discos': discos})

def compra(request):
    discos = Disco.objects.all()
    return render(request, 'compra.html', {'discos': discos})

def intercambia(request):
    return render(request, 'intercambia.html')

def coleccion(request):
    discos = Disco.objects.all()
    return render(request, 'coleccion.html', {'discos': discos})

def lista_discos(request):
    discos = Disco.objects.all()
    return render(request, 'index.html', {'discos': discos})

def detalle_disco(request, id):
    disco = get_object_or_404(Disco, id=id)
    return render(request, 'vista_disco.html', {'disco': disco})

def nuevo_disco(request):
    if request.method == "POST":
        form = DiscoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_discos')
    else:
        form = DiscoForm()
    return render(request, 'nuevo_disco.html', {'form': form})

def editar_disco(request, id):
    disco = get_object_or_404(Disco, id=id)
    if request.method == "POST":
        form = DiscoForm(request.POST, request.FILES, instance=disco)
        if form.is_valid():
            form.save()
            return redirect('lista_discos')
    else:
        form = DiscoForm(instance=disco)
    return render(request, 'editar_disco.html', {'form': form})

def eliminar_disco(request, id):
    disco = get_object_or_404(Disco, id=id)
    if request.method == "POST":
        disco.delete()
        return redirect('lista_discos')
    return render(request, 'eliminar_disco.html', {'disco': disco})

