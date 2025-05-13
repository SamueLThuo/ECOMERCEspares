from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deals', views.deals, name='deals'),
    path('about', views.about, name='about'),
    path('categories', views.categories, name='categories'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart_view, name='cart'), 
    path('login', views.login_view, name='login'), 
    path('signup/', views.signup_view, name='signup'),
    path('products/', views.signup_view, name='products'),
]