from django.urls import path
from .views import IndexView, Category_list, DetailView, Lastest_news, ContactUs, NewCreateView, NewUpdateView, DeleteView, SearchView, DeletePostView

app_name='home'
urlpatterns=[
    path('', IndexView.as_view(), name='home'),
    path('category/<int:id>/', Category_list.as_view(), name="category" ),
    path('detail/<int:id>/', DetailView.as_view(), name="detail"),
    path('las_news/<int:id>/', Lastest_news.as_view(), name="lastnews"),
    path('contact/', ContactUs.as_view(), name="contact"),
    path('newcreate/', NewCreateView.as_view(), name="newcreate"),
    path('newupdate/<int:id>/', NewUpdateView.as_view(), name="newupdate"),
    path('delete/<int:id>/', DeleteView.as_view(), name="delete"),
    path('delete-post/<int:id>/', DeletePostView.as_view(), name="delete-post"),
    path('search/', SearchView.as_view(), name="search"),
    
]