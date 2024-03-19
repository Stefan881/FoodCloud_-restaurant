from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index-url'),
    path('book_a_table', views.book_a_table, name='Book-a-table-url'),
    path('contact_us', views.contact, name='contact_us-url'),
    path('login',views.login_user,name='login-url'),
    path('base',views.base,name='base-url'),
    path('register_user',views.register_user,name='register_user-url'),
    path('buy_product/<id>',views.buy_product,name='buy_product-url'),
    path('grocery',views.grocery,name='grocery-url'),
    path('add_product',views.add_product,name='add_product-url'),
]
