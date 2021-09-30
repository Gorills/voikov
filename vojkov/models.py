from django.db import models
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