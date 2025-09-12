from django.shortcuts import render, redirect, get_object_or_404
import random
from .models import MensajesClub, Emociones, MiOpinion
from .forms import MensajesClubForm

# Create your views here.
def nuevo_mensaje(request):
    if request.method == 'POST':
        form = MensajesClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_mensaje')
    else:
        form = MensajesClubForm()
    
    return render(request, 'myapp/nuevo_mensaje.html', {'form': form})

def index(request):
    return render(request, 'myapp/index.html')

def mensajes_club(request):
    mensajes = MensajesClub.objects.all().order_by('-fecha')
    name = mensajes.first().nombre if mensajes.exists() else "Anonimo"
    return render(request, 'myapp/mensajes_club.html', {'nombre': name, 'mensajes': mensajes})

def mostrar_mensaje(request, pk):
    mensaje = get_object_or_404(MensajesClub, pk = pk)
    return render(request, 'myapp/mostrar_mensaje.html', {'mensaje': mensaje})


def mensajes_emociones(request):
    emociones = ['triste', 'preocupada', 'feliz', 'enojada', 'decepcionada']
    mensajes_por_emocion = {}

    for emocion in emociones:
        mensajes = Emociones.objects.filter(emocion__iexact = emocion)
        if mensajes.exists():
            mensajes_por_emocion[emocion] = random.choice(mensajes)
        else:
            mensajes_por_emocion[emocion] = None

    return render(request, 'myapp/mensajes_emociones.html', {'mensajes_por_emocion': mensajes_por_emocion})

def opinion_personal(request):
    mensajes = MiOpinion.objects.all()

    return render(request, 'myapp/opinion_personal.html', {'mensajes': mensajes})