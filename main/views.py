from django.shortcuts import render
from django.core.mail import send_mail
from dentora import settings
# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def contact_page(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message_message = request.POST['message-message']

        #send and email
        send_mail(
            subject=message_subject,
            message=message_message,
            from_email=message_email,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        context = {
            'message_name': message_name,
            'message_email': message_email,
            'message_subject': message_subject,
            'message_message': message_message,
        }

        return render(request, 'main/contact.html', context)
    else:
        return render(request, 'main/contact.html')


def about_page(request):
    return render(request, 'main/about.html')


def appointment_page(request):
    return render(request, 'main/appointment.html')


def price_page(request):
    return render(request, 'main/price.html')


def service_page(request):
    return render(request, 'main/service.html')


def team_page(request):
    return render(request, 'main/team.html')


def testimonial_page(request):
    return render(request, 'main/testimonial.html')
