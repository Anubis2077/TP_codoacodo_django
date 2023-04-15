from django.db import models
from datetime import datetime
from core.usuarios.choices import gender_choices

# Create your models here.

class client (models.Model):
    names= models.CharField(max_length=50, null=False,blank=False, verbose_name='Nombres')
    surnames= models.CharField(max_length=50, null=False,blank=False, verbose_name='Apellidos')
    dni= models.IntegerField(unique=True, null=False, help_text='introduzca su D.N.I. sin puntos', verbose_name='dni')
    bitrthday=models.DateField(verbose_name='fecha_de_nacimiento',null=True, blank=True)
    address=models.CharField(max_length=200, null=False, blank=False, verbose_name='domicilio')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


