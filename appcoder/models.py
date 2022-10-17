from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField(primary_key=True)
    telefono=models.IntegerField()
    cumpleaños=models.DateField(null = True)

    def __str__(self):
        return f"{(self.nombre)} {(self.apellido)} | {(self.cumpleaños)}"
