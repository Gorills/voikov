from django.db import models
from django.urls import reverse

# Create your models here.

class Layouts(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    project = models.CharField(max_length=50, verbose_name='Проект')
    
    home = models.DecimalField(verbose_name='Дом', max_digits=3, decimal_places=0)
    area = models.DecimalField(verbose_name='Площадь квартиры', max_digits=5, decimal_places=2)
    price = models.DecimalField(verbose_name='Цена от ...', max_digits=8, decimal_places=0)
    rooms = models.DecimalField(verbose_name='Количество комнат', max_digits=2, decimal_places=0)
    plan = models.ImageField(upload_to='layouts', verbose_name='Планировка')
    at_flore = models.ImageField(upload_to='layouts', verbose_name='На этаже')
    section = models.ImageField(upload_to='layouts', verbose_name='План секции')
    slug = models.SlugField(verbose_name='URL')
    side = models.ForeignKey('Side', related_name='layouts', verbose_name='Сторона света', on_delete=models.PROTECT, null=True, blank=True)
    home = models.ForeignKey('Home', related_name='lay', verbose_name='Дом', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("layouts_detail", kwargs={"slug": self.slug})
    


    class Meta:
        
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class Side(models.Model):
    name = models.CharField(verbose_name='Сторона света', max_length=50)
    img = models.ImageField(verbose_name='Изображение')


    def __str__(self):
        return self.name


    class Meta:
        
        verbose_name = 'Сторона света'
        verbose_name_plural = 'Стороны света'



class Home(models.Model):
    name = models.CharField(max_length=150, verbose_name='Дом')
    date = models.DateField(verbose_name='Перезача ключей')
    done = models.BooleanField(verbose_name='Сдан или нет')

    def __str__(self):
        return self.name


    class Meta:
        
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
