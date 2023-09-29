from django.forms import ModelForm
from django import forms
from .models import Reserva, Stand

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'cnpj': forms.TextInput(attrs={'class': 'form-control' }),
            'nome_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'stand': forms.Select(attrs={'class':'form-control'}),
        }
        
class StandForm (ModelForm):
    class Meta:
        model = Stand
        fields = '__all__'
        widgets ={
            'lacalizacao': forms.TextInput(attrs={'class':'form-control'}),
            'valor': forms.TextInput(attrs={'class':'form-control'}),
    }
       
