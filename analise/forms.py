from django import forms
from .models import ComentarioModel

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = ComentarioModel
        fields = ['texto']  # só o campo que o usuário vai preencher
        labels = {
            'texto': 'Digite seu comentário'
        }
        widgets = {
            'texto': forms.Textarea(attrs={
                "rows": 4,
                "class": "form-control",   # classe do Bootstrap
                "placeholder": "Escreva aqui seu comentário..."
            })
        }
