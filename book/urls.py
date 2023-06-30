from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show_book/', views.show_book, name='show_book'),
    path('borrow_book/<int:id>', views.borrow_book, name='borrow_book'),
    path('search_book/', views.search_book, name='search_book'),
    path('search/', views.search, name='search'),
    
]