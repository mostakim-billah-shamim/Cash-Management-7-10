from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm





class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    




class LoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    




class AddCashForm(forms.ModelForm):
    class Meta:
        model = AddCashModel
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    




class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = '__all__'
        exclude = ['user']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in self.fields.values():
            i.widget.attrs.update({'class': 'form-control'})
    