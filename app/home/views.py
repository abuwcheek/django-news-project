from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import View
from django.contrib import messages
from .models import Category, Tag, New, Contact
from django.views.generic.detail import DetailView
from .forms import NewCreateForm
from django.db.models import Q



class Lastest_news(View):
    def get(self, request, id):
        lastest_newsss = New.objects.all().order_by('-id')[:6]
        context={
            'lastest_news': lastest_news
        }
        return render(request, 'index.html', context)

class IndexView(View):
    def get(self, request):
        news=New.objects.all().order_by('-id')[:5]
        football_news=New.objects.filter(category__name='Futbol xabarlari')[:4]
        internal_news=New.objects.filter(category__name='Ichki yangiliklar')[:4]
        buizness_news=New.objects.filter(category__name='Buizness')[:4]
        global_news=New.objects.filter(category__name='Jaxon xabarlari')[:4]
        wheather_new=New.objects.filter(category__name='Ob-havo')[:4]
        day_news=New.objects.filter(category__name='Kundalik yangiliklar')[:4]
        lastest_news = New.objects.all().order_by('-id')[:6]
        famous_new = New.objects.all().order_by('-id')[:6]


        context={
            'football_news': football_news,
            'internal_news': internal_news,
            'buizness_news': buizness_news,
            'global_news': global_news,
            'wheather_new': wheather_new,
            'day_news': day_news,
            'lastest_news': news,
            'famous_new': famous_new
        }


        return render(request, 'index.html', context=context)




class Category_list(View):
    def get(self, request, id):

        ctg=Category.objects.get(id=id)
        # category_list=New.objects.filter(category__id=id)
        category_list=ctg.category_news.all()
        context={
            'ctg':ctg,
            'category_list':category_list
        }
        return render(request, 'category_list.html', context)



class DetailView(View):
    def get(self, request, id):
        news=get_object_or_404(New, id=id)
        news.views+=1
        news.save()

        context={
            'news': news,
        }
        return render(request, 'detail.html', context)



class ContactUs(View):
    def get(self, request):
        return render(request, 'contact.html')

    
    def post(self, request):
        data=request.POST
        contact=Contact()

        contact.name=data.get('name')
        contact.email=data.get('email')
        contact.subject=data.get('subject')
        contact.message=data.get('message')

        contact.save()

        return render(request, 'contact.html')
        



class NewCreateView(View):
    form=NewCreateForm()
    def get(self, request):
        if request.user.is_authenticated:
            form=NewCreateForm()
            return render(request, 'new_create.html', {'form':form})
        messages.error(request, 'Iltimos, saytga kiring!')
        return redirect('accounts:login')


    def post(self, request):
        form=NewCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new=form.save(commit=False)
            new.author=request.user
            new.save()
            messages.success(request, 'Yangilik yaratildi!')
            return redirect('home:home')
            
        messages.error(request, 'Yangilik yaratilmadi1')
        return render(request, 'new_create.html', {'form':form})


class NewUpdateView(View):

    def get(self, request, id):
        new=get_object_or_404(New, id=id)
        if request.user.is_authenticated and request.user == new.author:
            form=NewCreateForm(instance=new)
            return render(request, 'new_update.html', {'form':form})
        messages.error(request, 'Sizga ruxsat yoq!')
        return redirect('home:home')

    def post(self, request, id):
        new=get_object_or_404(New, id=id)
        form=NewCreateForm(data=request.POST, files=request.FILES, instance=new)
        if form.is_valid():
            new=form.save(commit=False)
            new.author=request.user
            new.save()
            messages.success(request, 'Yangilik ozgartirildi!')
            return redirect('home:home')
        messages.error(request, 'Yangilik ozgartirilmadi!')
        return render(request, 'new_update.html', {'form': form})



class DeleteView(View):
    def get(self, request, id):
        new=get_object_or_404(New, id=id)
        context={
            'news': new
        }
        return render(request, 'delete.html', context)
    

class DeletePostView(View):    
    def post(self, request, id):
            new=get_object_or_404(New, id=id)
            new.delete()
            messages.success(request, 'Yangilik ochirildi')
            return redirect('home:home')
    



from itertools import chain

class SearchView(View):
    def get(self, request):
        query=request.GET.get('query')
        if not query:
            return redirect('home:home')

        tag=get_object_or_404(Tag, name=query)
        new=New.objects.all().filter(Q(title__icontains = query) | Q(body__icontains = query))
        tag_news=tag.new_set.all()
        result_list=list(chain(tag_news, new))

        context={
            'searchnews': result_list,
        }
        return render(request, 'search.html', context)