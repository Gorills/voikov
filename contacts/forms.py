from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Contact


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()
    

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'popup-call__input',
                'placeholder': 'Имя'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'popup-call__input',
                'placeholder': '+7 (999) 999 99 99'
            }),

            
        }
        labels = {
            'name': '',
            'phone': '',
            

        }
