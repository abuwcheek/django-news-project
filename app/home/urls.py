from django.urls import path
from .views import IndexView, Category_list, DetailView, Lastest_news, ContactUs, NewCreateView, NewUpdateView, DeleteView, SearchView, DeletePostView

app_name='home'
urlpatterns=[
    path('', IndexView.as_view(), name='home'),
    path('category/<str:slug>/', Category_list.as_view(), name="category" ),
    path('detail/<str:slug>/', DetailView.as_view(), name="detail"),
    path('las_news/<str:slug>/', Lastest_news.as_view(), name="lastnews"),
    path('contact/', ContactUs.as_view(), name="contact"),
    path('newcreate/', NewCreateView.as_view(), name="newcreate"),
    path('newupdate/<str:slug>/', NewUpdateView.as_view(), name="newupdate"),
    path('delete/<str:slug>/', DeleteView.as_view(), name="delete"),
    path('delete-post/<str:slug>/', DeletePostView.as_view(), name="delete-post"),
    path('search/', SearchView.as_view(), name=""),
    
]