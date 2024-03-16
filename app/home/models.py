from django.db import models
from app.accounts.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.


class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    class Meta:
# mavhumlik, ya'ni boshqa modellarga o'xshab modelni bazaga yozmaydi faqat meros olib ishlatiladi
        abstract=True



class Category(BaseModel):
    name=models.CharField(max_length=50)
    slug=models.SlugField(verbose_name='slug')

    def __str__(self):
        return self.name



class Tag(BaseModel):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name



class New(BaseModel):
    title=models.CharField(max_length=200)
    slug=models.SlugField(verbose_name="slug", null=True, unique=True)
    views=models.IntegerField(default=0)
    image=models.ImageField(upload_to="news_images/")
    body=RichTextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_news')
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='category_news')
    tags=models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return f"{self.author} - {self.title}"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)


class About(BaseModel):
    linkedin=models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    youtube=models.CharField(max_length=100)
    instagram=models.CharField(max_length=100)
    twitter=models.CharField(max_length=100)
    email=models.EmailField()
    locations=models.CharField(max_length=500)
    phone=models.CharField(max_length=20)



    def __str__(self):
        return "About"




class Contact(BaseModel):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()


    def __str__(self):
        return self.name
    


class Ads(BaseModel):
    choises_pos=(
        ('one', 'ONE'),
        ('two', 'TWO'),
    )
    image=models.ImageField(upload_to='ads_images/')
    link=models.CharField(max_length=150)
    position=models.CharField(max_length=5, choices=choises_pos)