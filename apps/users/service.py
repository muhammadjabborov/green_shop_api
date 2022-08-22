# import threading
#
# from django.contrib.sites.shortcuts import get_current_site
# from django.urls import reverse
# from rest_framework_simplejwt.tokens import RefreshToken
#
# from apps.users.models import User
# from django.core.mail import EmailMessage
#
# import threading
#
#
# class EmailThread(threading.Thread):
#
#     def __init__(self, email):
#         self.email = email
#         threading.Thread.__init__(self)
#
#     def run(self):
#         self.email.send()
#
#
# class Util:
#     @staticmethod
#     def send_email(request, email):
#         user = User.objects.get(email=email)
#         message_data = {
#             'message': 'Please check your email'
#         }
#         current_site = get_current_site(request).domain
#         relativeLink = reverse('email-verify')
#         absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
#         email_body = 'Hi ' + user.username + \
#                      ' Use the link below to verify your email \n' + absurl
#         data = {'email_body': email_body, 'to_email': user.email,
#                 'email_subject': 'Verify your email'}
#
#         EmailThread(data).start()
#         return message_data
