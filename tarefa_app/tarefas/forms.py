from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task, TimeEntry
from django.utils import timezone

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu nome de usuário'
        })
    )
    password1 = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )
    password2 = forms.CharField(
        label='Confirmação de Senha',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirme sua senha'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    inicio = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            },
            format='%Y-%m-%dT%H:%M'
        ),
        required=True
    )
    fim = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control',
            },
            format='%Y-%m-%dT%H:%M'
        ),
        required=False
    )
    
    class Meta:
        model = Task
        fields = ['titulo', 'descricao', 'inicio', 'fim']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),  
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),  
        }


class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ['duracao', 'descricao']
        widgets = {
            'duracao': forms.TimeInput(attrs={'type': 'time'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
