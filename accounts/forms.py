from django import forms
from django.forms import widgets
from django.forms.widgets import PasswordInput
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Enter Password',
    }))

    confirm_password = forms.CharField(widget=PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Confirm Password',
    }))


    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'      
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'      
            self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'      
            self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'      
            self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'      

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        pasword = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if pasword != confirm_password:
            raise forms.ValidationError('Passwords does not match')
