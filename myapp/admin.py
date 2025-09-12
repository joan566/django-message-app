from django.contrib import admin
from .models import MensajesClub, Emociones, MiOpinion

@admin.register(MensajesClub)
class MensajesClubAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contenido', 'fecha')

@admin.register(Emociones)
class EmocionesAdmin(admin.ModelAdmin):
    list_display = ('emocion', 'mensaje')

@admin.register(MiOpinion)
class MiOpinionAdmin(admin.ModelAdmin):
    list_display = ('mensaje', )
