from __future__ import absolute_import
from celery import shared_task

from django.core.mail import send_mail

@shared_task
def send_email_notification(to, subject, text):
    send_mail(subject, text, 'a1tt@rambler.ru', [to], fail_silently=False)