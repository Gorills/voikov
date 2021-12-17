from typing import Text
from django.db import models
from django.urls import reverse
from django.db.models.fields import CharField

# Create your models here.

class Doc(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название документа')
    file = models.FileField(upload_to='uploads')
    parent = models.ForeignKey('DocCat', verbose_name='Категория документов', related_name='doc', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class DocCat(models.Model):
    name = models.CharField(max_length=250, verbose_name='Категория документов')

    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = 'Категория документа'
        verbose_name_plural = 'Категория документов'


class Page(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    h1 = models.CharField(max_length=250, blank=True, null=True, verbose_name='Заголовок H1')
    text = models.TextField()
    top_menu = models.BooleanField(null=True, blank=True, verbose_name='Главное меню')
    
    drop_menu_left = models.BooleanField(max_length=300, null=True, blank=True, verbose_name='Выпадающее меню покупателям')
    drop_menu_right = models.BooleanField(max_length=300, null=True, blank=True, verbose_name='Выпадающее меню о нас')

    footer_menu = models.BooleanField(null=True, blank=True, verbose_name='Футер')
    metatitle = models.CharField(max_length=250, verbose_name='Мета заголовок')
    metadesc = models.CharField(max_length=250, verbose_name='Мета описание')
    metakey = models.CharField(max_length=250, verbose_name='Ключевые слова')
    slug = models.SlugField(null=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("page", kwargs={"slug": self.slug})
    

    class Meta:
        
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'



class PageBlock(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название/заголовок')
    text = models.TextField()
    color = models.CharField(max_length=10, verbose_name='Цвет')
    page = models.ForeignKey(Page, related_name='block', verbose_name='Страница', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'



class HomeBlock(models.Model):
    title = models.CharField(max_length=250, verbose_name='Навание')
    desc = models.CharField(max_length=300, verbose_name='Короткое описание')
    text = models.TextField(verbose_name='Полное описание')
    slider = models.BooleanField(verbose_name='Слайдер')
    solo = models.BooleanField(verbose_name='Одна картинка')
    grid = models.BooleanField(verbose_name='Сетка 4 фото')

    def __str__(self):
        return self.title

    class Meta:
        
        verbose_name = 'Блок на главной'
        verbose_name_plural = 'Блоки на главной'


class HomeBlockImages(models.Model):
    parent = models.ForeignKey(HomeBlock, related_name='images', verbose_name='Блок', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/block')


    class Meta:
        
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'





class HodBlock(models.Model):
    title = models.CharField(max_length=250, verbose_name='Навание')
    desc = models.CharField(max_length=300, verbose_name='Короткое описание')
    text = models.TextField(verbose_name='Полное описание')
    slider = models.BooleanField(verbose_name='Слайдер')
    solo = models.BooleanField(verbose_name='Одна картинка')
    grid = models.BooleanField(verbose_name='Сетка 4 фото')

    def __str__(self):
        return self.title

    class Meta:
        
        verbose_name = 'Ход строительства'
        verbose_name_plural = 'Ход строительства'


class HodBlockImages(models.Model):
    parent = models.ForeignKey(HodBlock, related_name='images', verbose_name='Блок', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/block')


    class Meta:
        
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'



class Ipoteka(models.Model):
    name = models.CharField(max_length=250)
    persent = models.CharField(max_length=20)


    def __str__(self):
        return self.name


    class Meta:
        
        verbose_name = 'Ипотека'
        verbose_name_plural = 'Ипотеки'


class Banks(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='images/banks')


    def __str__(self):
        return self.name


    class Meta:
        
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'