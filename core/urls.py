from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.index,name='home'),
    path('about/',views.about, name='about'),
    path('blog/',views.blog,name='blog'),
    path('chefs/',views.chefs,name='chefs'),
    path('contact/',views.contact,name='contact'),
    path('elements/',views.elements,name='elements'),
    path('food/',views.food_menu,name='food'),
    path('single_blog/',views.single_blog,name='single'),
    path('signup/',views.sign_up,name='signup'),
    path('',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout')
]
