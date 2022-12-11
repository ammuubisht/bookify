from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [ 
    path('', homepage, name='homepage' ),
    path('book/<slug:slug>', book_detail, name='book-detail-page'),
    path('login', loginPage, name='login'),
    path('signup', signupPage, name='signup'),
    path('logout', logoutUser, name='logout'),
    path('profile', profilePage, name='profile-page'),
]

