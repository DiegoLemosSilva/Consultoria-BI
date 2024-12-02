# forms.py
from django import forms
from .models import model_db_CheckinI,model_db_cardapio,upload_photo_chekin

class PhotoFormCheckin(forms.ModelForm):
    class Meta:
        model = upload_photo_chekin
        fields = ['estabelecimento','cidade','estado', 'img']





    



