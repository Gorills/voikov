from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    page = models.CharField(max_length=150, verbose_name='Страница')

    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'