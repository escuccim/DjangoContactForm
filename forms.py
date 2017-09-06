from  django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class BootstrapModelForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ContactForm(BootstrapModelForm):
    name = forms.CharField(label=_("Name"),max_length=128, required=True)
    subject = forms.CharField(label=_("Subject"),max_length=128, required=True)
    email = forms.EmailField(required=True, label=_("Email"))
    message = forms.CharField(widget=forms.Textarea, required=True, label=_("Message"))