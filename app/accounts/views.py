from django.shortcuts import render, redirect
from django.views import View
from .forms import CastumAuthForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import User
from PIL import Image

# Create your views here.


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:home')
        form=CastumAuthForm
        context={
            'form': form,
        }

        return render(request, 'accounts/login.html', context)

    
    def post(self, request):
        data=request.POST
        form=CastumAuthForm(data=data)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            messages.success(request, 'Tizimga muvaffaqqiyatli kirdingiz.')
            return redirect('home:home')
        else:
            messages.warning(request, 'Parol yoki login xato.')
            return render(request, 'accounts/login.html', {'form':form})



class LogoutView(View):
    
    def get(self, request):
        logout(request)
        messages.info(request, 'Tizimdan muvaffaqqiyatli chiqtingiz.')
        return redirect('home:home')




class UserRegisterView(View):
    form=UserRegisterForm
    def get(self, request):
        if not request.user.is_authenticated:
                
            context={
                'form':self.form,
            }

            return render(request, 'accounts/register.html', context)
        messages.warning(request, 'Siz avval tizimdan chiqishingiz kerak.')
        return redirect('home:home')

    def post(self, request):
        user_form=self.form(data=request.POST, files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Akaunt muvaffaqqiyatli yaratildi.')
            return redirect('home:home')
        messages.warning(request, 'Akaunt yaratilmadi.')
        context={
            'form':user_form,
        }
        return render(request, 'accounts/register.html', context)



class MyProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user=User.objects.get(id=request.user.id)
            context={
                'user': user,
            }
            return render(request, 'accounts/profile.html', context)
        messages.warning(request, 'Siz oldin Login qilishingiz kerak.')
        return redirect('accounts:login')




class UserUpdateView(View):
    form=UserUpdateForm
    def get(self, request):
        if request.user.is_authenticated:
            user=User.objects.get(id=request.user.id)
            context={
                'form': self.form(instance=user),
            }
            return render(request, 'accounts/update.html', context)

        messages.warning(request, 'Siz oldin tizimga kirishingiz kerak.')
        return redirect('home:home')

    def post(self, request):
        user_form=self.form(data=request.POST, files=request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Akaunt muvaffaqiyatli yangilandi.')
            return redirect('home:home')
        messages.warning(request, 'Akaunt yangilanmadi.')
        context={
            'form': user_form,
        }
        return render(request, 'accounts/update.html', context)