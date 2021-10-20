from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.db import models

from .models import Doc, DocCat, Page, PageBlock, HomeBlock, HomeBlockImages
# Register your models here.


admin.site.register(Doc)
admin.site.register(DocCat)

class PageAdminForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Page
        fields = '__all__'



class PageBlockForm(forms.ModelForm):
    text = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = PageBlock
        fields = '__all__'
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
            
        }


class PageBlockAdmin(admin.StackedInline):
    model = PageBlock
    form = PageBlockForm
    extra = 0
    min_num = 0

    


class PageAdmin(admin.ModelAdmin):
    inlines = [
        PageBlockAdmin,
    ]
    form = PageAdminForm
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Page, PageAdmin)



class HomeImagesAdmin(admin.TabularInline):
    model = HomeBlockImages
    extra = 0
    min_num = 0

class HomeBlockAdmin(admin.ModelAdmin):

    inlines = [
        HomeImagesAdmin,
    ]

admin.site.register(HomeBlock, HomeBlockAdmin)