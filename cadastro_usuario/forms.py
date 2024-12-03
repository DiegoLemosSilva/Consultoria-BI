# forms.py
from django import forms
from .models import upload_photo_chekin

class PhotoFormCheckin(forms.ModelForm):

    class Meta:
        model = upload_photo_chekin
        fields = ['nome_campanha','nome_produto','protocolo','data','img']
        widgets = {
            'nome_campanha':forms.TextInput(attrs={'class': 'form-control'}),
            'nome_produto':forms.TextInput(attrs={'class': 'form-control'}),
            'protocolo':forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(
                attrs={
                    'class': 'form-control datepicker',  # Classe associada ao Datepicker
                    'placeholder': 'Selecione uma data'
                }
            )
            
        }





    



