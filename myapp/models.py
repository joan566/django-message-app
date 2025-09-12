from django.db import models

# Create your models here.

class MensajesClub(models.Model):
    nombre = models.CharField(max_length = 100)
    contenido = models.TextField("Contenido del mensaje")
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.nombre} - {self.contenido[:50]}"
    
class Emociones(models.Model):
    emocion = models.CharField(max_length = 100, null= True, blank= True)
    mensaje = models.TextField()

    def __str__(self):
        return f"{self.emocion} - {self.mensaje[:30]}"

class MiOpinion(models.Model):
    mensaje = models.TextField(default = "No hay un mensaje aun.")

    def __str__(self):
        return f"{self.mensaje}"