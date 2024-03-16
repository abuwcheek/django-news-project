from django.urls import path
from .views import LoginView, LogoutView, UserRegisterView, MyProfileView, UserUpdateView


app_name='accounts'
urlpatterns=[
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', MyProfileView.as_view(), name='profile'),
    path('update/', UserUpdateView.as_view(), name='update'),
]