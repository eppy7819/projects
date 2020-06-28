from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(
        max_length = 10,
    label = '닉네임',
    help_text='닉네임을 10자 이내로 작성하세요.',
    widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'placeholder': '닉네임 입력',
            }
        )
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'nickname']

class ProfileUpdateForm(ModelForm):  # UserCreationForm
    nickname = forms.CharField(
    max_length = 10,
    label = '닉네임',
    help_text='닉네임을 10자 이내로 작성하세요.',
    widget=forms.TextInput(
            attrs={
                'class': 'my-input',
                'placeholder': '닉네임 입력',
            }
        )
    )
    introduction = forms.CharField(
            label='자기소개',
            help_text='자신에 대한 소개를 자유롭게 작성해주세요.',
            widget=forms.Textarea(
                    attrs={
                        'row':5,
                        'col':50,
                    }
                ))
    
    
    class Meta:
        model = User
        fields = ['nickname', 'introduction',]