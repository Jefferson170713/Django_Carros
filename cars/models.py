from django.db import models

# Criando a 2° tabela para chave estrangeira
class Brand(models.Model):
    id = models.AutoField( primary_key=True , verbose_name='ID_MARCA' )
    name = models.CharField( max_length=150 , verbose_name='MARCA' )

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['name']

    def __str__(self):
        return self.name
# criando a 1° tabela Car
class Car(models.Model):
    id = models.AutoField( primary_key=True , verbose_name='ID_CARRO' )
    model = models.CharField( max_length=150 , verbose_name='MODELO' )
    brand = models.ForeignKey( 
        Brand,
        on_delete=models.PROTECT, 
        related_name='car_brand', 
        verbose_name='MARCA'
        )
    factory_year = models.IntegerField( blank=True, null=True, verbose_name='ANO DE FABRICAÇÃO' )
    model_year = models.IntegerField( blank=True, null=True, verbose_name='ANO DO MODELO' )
    plate = models.CharField( max_length=10, blank=True, null=True , verbose_name='PLACA' )
    value = models.FloatField( blank=True, null=True , verbose_name='VALOR' )
    photo = models.ImageField( 
        upload_to='Cars/', 
        blank=True, 
        null=True,
        verbose_name='FOTO' 
        )

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['model']


    def __str__( self ):
        return f'{self.model} - {self.brand}'