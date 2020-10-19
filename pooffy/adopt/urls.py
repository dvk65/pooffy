from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog_home/', views.blog_home, name='blog_home'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('cats/', views.cats, name='cats'),
    path('contact/', views.contact, name='contact'),
    path('dogs/', views.dogs, name='dogs'),
    path('elements/', views.elements, name='elements'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('adoptee/',views.adoptee,name='adoptee')
]