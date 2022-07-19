from dataclasses import field
from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Ingrese Contraseña',
        'class' : 'form-control'
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirmar Contraseña',
        'class' : 'form-control'
    }))
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        
    
    def __init__(self, *arg, **kwargs):
        super(RegistrationForm, self).__init__(*arg, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Número de teléfono'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'