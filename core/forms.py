from django import forms
from django.contrib.auth.models import User

from .models import *

class MessageForm(forms.ModelForm):

    content = forms.CharField(label = 'Mensagem', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'style': 'height: 100px;',}))
    
    class Meta:
        model = Message
        fields = ['content']
    

class NewMessageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewMessageForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['addressee'].queryset = User.objects.exclude(pk=self.user.pk)

    content = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'style': 'height: 100px;',
    }))

    addressee = forms.ModelChoiceField(label='Destinatário', queryset=User.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Message
        fields = ['content', 'addressee']

