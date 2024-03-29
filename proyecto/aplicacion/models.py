from django.db import models

# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    dni = models.IntegerField()

    class Meta:
        ordering = ["dni"]

    def str(self):
        return f"{self.nombre}, {self.apellido}"


class Cheques(models.Model):
    banco = models.CharField(max_length=30)
    fecha = models.DateField()
    monto = models.IntegerField()
    numero = models.IntegerField()
    perteneciente = models.IntegerField() #se refiere a la visibilidad. cada usuario tiene una id, y el objeto solo sera visible si le pertenece.

    class Meta:
        ordering = ["numero"]

    def str(self):
        return f"{self.numero}"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    dni = models.IntegerField()
    empresa = models.CharField(max_length=40)
    class Meta:
        ordering = ["dni"]

    def str(self):
        return f"{self.apellido}, {self.empresa}"
    

class PagoPendiente(models.Model):
    deudor = models.CharField(max_length=30)
    vencimiento = models.DateField()
    monto = models.IntegerField()
    numero = models.IntegerField()
    perteneciente = models.IntegerField()
    
    class Meta:
        ordering = ["numero"]

    def str(self):
        return f"{self.deudor}, {self.monto}"