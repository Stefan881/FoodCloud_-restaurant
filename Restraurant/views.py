from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from FoodCloud_Restraurant.settings import EMAIL_HOST_USER


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
