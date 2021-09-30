from django.contrib import admin
from django.forms import ModelForm, FileField

from .models import Layouts, Side, Home
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Home, HomeAdmin)



class SideModelForm(ModelForm):
    class Meta:
        model = Side
        exclude = []
        field_classes = {
            'img': FileField,
            

        }

class SideAdmin(admin.ModelAdmin):
    form = SideModelForm

admin.site.register(Side, SideAdmin)


class LayoutsModelForm(ModelForm):
    class Meta:
        model = Layouts
        exclude = []
        field_classes = {
            'plan': FileField,
            'at_flore': FileField,
            'section': FileField,

        }



class LayoutsAdmin(admin.ModelAdmin):
    form = LayoutsModelForm
    prepopulated_fields = {'slug': ('name', 'area')}


admin.site.register(Layouts, LayoutsAdmin)