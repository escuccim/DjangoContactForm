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

def Contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_name = request.POST.get('name', '')
            contact_email = request.POST.get('email', '')
            contact_content = request.POST.get('message', '')
            contact_subject = request.POST.get('subject', '')

            template = get_template('contact/contact_template.txt')
            context = {'contact_name': contact_name,'contact_email': contact_email,'form_content': contact_content,}
            content = template.render(context)

            email = EmailMessage("New contact form submission",content,"Your website" + '',['skooch@gmail.com'],headers={'Reply-To': contact_email})
            email.send()

            contact_form = ContactForm()
            return render(request, 'contact/contact.html', { 'contact_form' : contact_form, 'message' : 'Your message has been sent'})
        else:
            print contact_form.errors

    else:
        contact_form = ContactForm()

    return render(request, 'contact/contact.html', { 'contact_form' : contact_form, 'message' : None})
