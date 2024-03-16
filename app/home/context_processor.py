from .models import Category, Tag, About,Ads

def index_processor(request):
    about=About.objects.first()
    kategoriyalar=Category.objects.all()
    tags=Tag.objects.all()[:20]
    ads_one=Ads.objects.all().filter(position='one', is_active=True).order_by('?')  
    ads_two=Ads.objects.all().filter(position='two', is_active=True).order_by('?')[:2]

    context={

        'kategoriyalar': kategoriyalar,
        'tags': tags,
        'about': about,
        'ads_one': ads_one,
        'ads_two': ads_two,
    }
    return context