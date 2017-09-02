# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.conf import settings
from django.template import loader

def Contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_name = request.POST.get('name', '')
            contact_email = request.POST.get('email', '')
            contact_content = request.POST.get('message', '')
            contact_subject = request.POST.get('subject', '')
            message_details = {'contact_name': contact_name,'contact_email': contact_email,'form_content': contact_content}

            html_message = loader.render_to_string('contact/contact_template.html', message_details)

            send_mail(contact_subject, contact_content, contact_email, [settings.DEFAULT_FROM_EMAIL], fail_silently=False, html_message=html_message)

            contact_form = ContactForm()
            return render(request, 'contact/contact.html', { 'contact_form' : contact_form, 'message' : 'Your message has been sent'})
        else:
            errors = contact_form.errors

    else:
        contact_form = ContactForm()

    context_dict = { 'contact_form' : contact_form, 'message' : None}

    return render(request, 'contact/contact.html', context_dict )
