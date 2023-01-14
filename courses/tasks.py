from DjangoProjectHillel.celery import app
from django.core.mail import send_mail
from courses.models import Student, DelayedMail
from rest_framework.authtoken.models import Token
from os import system


@app.task
def send_emails(data):
    emails = Student.objects.exclude(email__isnull=True).values_list('email', flat=True)
    message = f"""
Name: {data['name']}
Description: {data['description']}
Teacher: {data['teacher']}
"""
    for email in emails:
        send_mail(
            subject=f'*** New course ***',
            from_email='no-replay@email.com',
            message=message,
            recipient_list=[email]
        )


@app.task
def daily_mail():
    emails = Student.objects.exclude(email__isnull=True).values_list('email', flat=True)
    courses = DelayedMail.objects.all().values_list('name', flat=True)
    message = f"""
New courses today:  
{','.join(courses)}   
"""
    for email in emails:
        send_mail(
            subject='Here new courses',
            from_email='no-replay@email.com',
            message=message,
            recipient_list=[email]
        )
    DelayedMail.objects.all().delete()


@app.task
def refresh_token():
    users = Token.objects.select_related().values_list('user__username', flat=True)
    for username in users:
        system(f'python manage.py drf_create_token -r {username}')

