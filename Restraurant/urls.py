from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-url'),
    path('book_a_table', views.book_a_table, name='Book-a-table-url'),
    path('contact_us', views.contact, name='contact_us-url')
]
