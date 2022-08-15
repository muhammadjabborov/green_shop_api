import threading

from django.core.mail import EmailMessage

from app.products.models import JoinUser


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(email):
        message_data = {'message': 'Successful, please check your email'}
        user_join = JoinUser.objects.get(email=email)
        email_subject = 'Hi ' + user_join.email
        email_body = 'Sodiq KOOOT'
        data = {
            'email_subject': email_subject,
            'email_body': email_body,
            'to_email': user_join.email
        }
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']]
        )
        EmailThread(email).start()
        return message_data

