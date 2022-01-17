from django.db import models

# Create your models here.
class Caja(models.Model):
    tipo_estado=[('EN','Entrada'),('SA','Salida')]
    monto =models.FloatField()
    tipo=models.CharField(max_length=2,
                          choices=tipo_estado,
                          default='EN')
    fecha=models.DateTimeField(auto_now_add=True)