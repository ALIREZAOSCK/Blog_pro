from django import forms
from django.core.validators import ValidationError
from .models import Message


class ContactUsForm(forms.Form):
    years =['1999','2000','2011']
    name = forms.CharField(max_length=10, label='what is your name?')
    text = forms.CharField(max_length=10, label='write your message?')
    birthday = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('text and name are same',code='text_same_name')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'a' in name:
            raise ValidationError('you cant use a in name', code='a_in_name')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name please'
            }),
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your text  please'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email please'
            })
        }
