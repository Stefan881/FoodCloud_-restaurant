from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from FoodCloud_Restraurant.settings import EMAIL_HOST_USER
from .forms import SignUpForm, ProductForm
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth import login
from .models import Product
from django.http import HttpResponse
from django.contrib.sites import requests
from .credentials import *


# Create your views here.
def home(request):
    return render(request, 'index.html', {})


def book_a_table(request):
    if request.method == 'POST':
        client_name = request.POST['name']
        client_email = request.POST['email']
        client_phone = request.POST['phone']
        date_order = request.POST['date']
        order_time = request.POST['time']
        no_of_people = request.POST['people']
        message = request.POST['message']

        subject = 'Table Booking Request'
        message = f'Name: {client_name}\nEmail: {client_email}\nPhone: {client_phone}\nDate: {date_order}\nTime: {order_time}\nNumber of People: {no_of_people}\nMessage: {message}'

        # Send the email
        # Send the email
        send_mail(
            subject,
            message,
            client_email,
            ['ondeyostephen0@gmail.com'],  # Replace with recipient email address
        )
        return render(request, 'Book-a-table.html', {'client_name': client_name})

    return render(request, 'Book-a-table.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        # SEND AN EMAIL

        send_mail(
            message_name,
            message,
            message_email,
            ['ondeyostephen0@gmail.com'],
        )
        return render(request, 'contact.html', {'message_name': message_name})

    return render(request, 'contact.html', {})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Auhenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully Registered!Welcome')
            return redirect('index-url')
        else:
            form = SignUpForm()
            return render(request, 'register_user.html', {'form': form})

    return render(request, 'register_user.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!...')
            return redirect('index-url')
        else:
            messages.success(request, 'There was an error logging in.Please try again!...')
            return redirect('login-url')

    return render(request, 'login.html', {})


def base(request):
    return render(request, 'base.html', {})


def buy_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        phone = request.POST['phone']
        amount = product.price
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "PYMENT001",
            "TransactionDesc": "School fees"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Your Payment Request Was Successful")
    return render(request, 'buy_product.html', {'product': product})


def grocery(request):
    return render(request, 'Grocery.html', {})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The product has been successfully added!...')
            return redirect('grocery-url')
        else:
            messages.error(request, 'Product saving failed')
            return redirect('add_product-url')
    else:
        form = ProductForm()
        return render(request, 'Add_product.html', {})
