from django.db import models
from django.urls import reverse


class Room(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='room')
    slug = models.SlugField()
    min_price = models.CharField(max_length=20, verbose_name='Минимальная цена')
    min_area = models.CharField(max_length=20, verbose_name='Минимальная площадь')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("room", kwargs={"slug": self.slug})

    class Meta:
        
        verbose_name = 'Комнат в квартире'
        verbose_name_plural = 'Комнаты в квартире'



class Layouts(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    project = models.CharField(max_length=200, verbose_name='Проект')
    
    
    area = models.CharField(max_length=200, verbose_name='Площадь квартиры')
    price = models.CharField(max_length=200, verbose_name='Цена от ...')
    rooms = models.CharField(max_length=200, verbose_name='Количество комнат')
    etazhi = models.CharField(max_length=200, verbose_name='Этажи', null=True, blank=True)

    plan = models.ImageField(upload_to='layouts', verbose_name='Планировка')
    etazh = models.ImageField(upload_to='layouts', verbose_name='Поэтажная планировка', null=True, blank=True)
    etazh_mob = models.ImageField(upload_to='layouts/mob', verbose_name='Поэтажная планировка(мобильная версия)', null=True, blank=True)

    slug = models.SlugField(verbose_name='URL')
    side = models.ForeignKey('Side', related_name='layouts', verbose_name='Сторона света', on_delete=models.PROTECT, null=True, blank=True)
    home = models.ForeignKey('Home', related_name='lay', verbose_name='Дом', on_delete=models.CASCADE)

    ipoteka = models.CharField(max_length=200, verbose_name='Ипотека от..')

    activ = models.BooleanField(verbose_name='Активность', default=True)
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
    date = models.DateField(verbose_name='Передача ключей')
    done = models.BooleanField(verbose_name='Сдан или нет')

    def __str__(self):
        return self.name


    class Meta:
        
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
