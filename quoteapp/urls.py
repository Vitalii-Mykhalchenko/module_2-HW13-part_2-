from django.urls import path
from . import views


app_name = 'quoteapp'


urlpatterns = [
    path('', views.main, name='main'),
    path('quote/', views.quote, name='quote'),
    path('author/', views.author, name='author'),
    path('tag/', views.tag, name='tag'),
    path('<int:page>', views.main, name='main_paginate'),
    path('detail/<int:author_id>', views.detail, name='detail')

]



