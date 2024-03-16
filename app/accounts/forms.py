from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput,PasswordInput,EmailInput
from PIL import Image
from .models import User

class CastumAuthForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'email/phone number'}))
    password=forms.CharField(widget=PasswordInput(attrs={'placeholder':'password'}))


class UserRegisterForm(forms.ModelForm):
    username=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'username'}))
    first_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Abdullo'}))
    last_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Istamov'}))
    email=forms.EmailField(widget=EmailInput(attrs={'class':'validate', 'placeholder':'user@user.com'}))
    phone=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'+998937151034'}))
    avatar=forms.ImageField()


    password=forms.CharField(widget=PasswordInput(attrs={'class':'validate', 'placeholder':'password'}))
    confirm_password=forms.CharField(widget=PasswordInput(attrs={'class':'validate', 'placeholder':'confirm password'}))



    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'phone', 'avatar')



    def clean_username(self):
        username=self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu username oldin tizimda ro\'yxatdan o\'tgan')
        return username


    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password!=confirm_password:
            raise('Parollar bir biriga mos emas')
        return confirm_password

    
    def save(self, commit=True):
        user=super().save(commit)
        user.set_password(self.cleaned_data['confirm_password'])
        user.save()
        return user


        img=Image.open(user.avatar.path)
        
        if img.height>500 or img.width>500:
            new_img=(350,350)
            img.thumbnail(new_img)
            img.save(user.avatar.path)

            return user



class UserUpdateForm(forms.ModelForm):
    first_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Abdullo'}))
    last_name=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'Istamov'}))
    email=forms.EmailField(widget=EmailInput(attrs={'class':'validate', 'placeholder':'user@user.com'}))
    phone=forms.CharField(widget=TextInput(attrs={'class':'validate', 'placeholder':'+998937151034'}))
    avatar=forms.ImageField()


    class Meta:
        model=User
        fields=('first_name', 'last_name', 'email', 'phone', 'avatar')


     
    def save(self, commit=True):
        user=super().save(commit)
        user.save()


        img=Image.open(user.avatar.path)
        
        if img.height>500 or img.width>500:
            new_img=(350,350)
            img.thumbnail(new_img)
            img.save(user.avatar.path)
        
        return user
