#encoding:utf-8
import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context
import threading

class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
        msg.send(self.fail_silently)

def send_mail(subject, body, from_email, recipient_list, fail_silently=False, html=None, *args, **kwargs):
    EmailThread(subject, body, from_email, recipient_list, fail_silently, html).start()

def send_info_email(to, context_dict):
    t = loader.get_template('email_content.html')
    c = Context(context_dict)
    html = t.render(c)
    with open(os.path.join(settings.BASE_DIR, 'ssmanagement/templates/email_subject.txt'), 'r') as f:
        subject = f.read()
    EmailThread(subject, '', settings.DEFAULT_FROM_EMAIL, [to], fail_silently=True, html=html).start()
