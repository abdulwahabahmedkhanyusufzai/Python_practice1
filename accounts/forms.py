from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'age', 'pin', 'email', 'balance']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '4-digit PIN'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Initial Balance'}),
        }

class TransactionForm(forms.Form):
    amount = forms.IntegerField(
        min_value=1, 
        max_value=100000, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'})
    )
    pin = forms.IntegerField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Verify PIN'})
    )
