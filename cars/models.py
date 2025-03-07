from django.db import models

# criando o modelo Car
class Car(models.Model):
    id = models.AutoField( primary_key=True )
    model = models.CharField( max_length=150 )
    brand = models.CharField( max_length=150 )
    factory_year = models.IntegerField( blank=True, null=True)
    model_year = models.IntegerField( blank=True, null=True)
    value = models.FloatField( blank=True, null=True )

    def __str__( self ):
        return f'{self.model} - {self.brand}'