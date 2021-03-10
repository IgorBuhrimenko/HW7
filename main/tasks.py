from celery import shared_task

from django.template.loader import render_to_string
from sendgrid import Mail, SendGridAPIClient

from HW5.settings import SENDGRID_KEY, EMAIL_SENDER
from logger.models import Log


@shared_task
def send_email(data):
    context = {
        'name': data['name'],
        'email': data['email'],
        'message': data['text_message']
    }
    content = render_to_string('emails/getmessage.html', context)
    message = Mail(
        from_email=EMAIL_SENDER,
        to_emails='bugrimenkoim@gmail.com',
        subject='Added new comment',
        html_content=content
    )
    sg = SendGridAPIClient(SENDGRID_KEY)
    sg.send(message)


@shared_task
def clear_log():
    Log.objects.all().delete()
