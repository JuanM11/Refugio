from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Adoptante(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    cel=models.CharField(max_length=15)
    email=models.EmailField()
    direccion=models.TextField(max_length=50)
    mascota_a_adoptar=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('adoptante-list')
class Tipo(models.Model):
    TIPO = (('perros','Perros'),('gatos','Gatos'),('otros','Otros'))
    nombre=models.CharField(max_length=50,choices=TIPO)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('tipo-list')


 	
class Mascota(models.Model):
    adoptante=models.ForeignKey(Adoptante,null=True,blank=True,on_delete=models.PROTECT)
    tipo=models.ForeignKey(Tipo,null=False,blank=True,on_delete=models.PROTECT)
    nombre=models.CharField(max_length=50)
    SEXO = (('hembra','Hembra'),('macho','Macho')) 
    sexo=models.CharField(max_length=15,choices=SEXO)
    edad=models.IntegerField()
    raza=models.CharField(max_length=50)
    foto=models.ImageField(upload_to='')
    adoptado=models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('mascota-list')

@receiver(post_delete, sender=Mascota)
def mascota_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.foto.delete(False)

