from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(label = 'Mensagem', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'style': 'height: 100px;',}))