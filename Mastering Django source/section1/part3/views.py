from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm
from .mixins import OnlyStaffMixin


class ContactNew(OnlyStaffMixin, CreateView):
    model = Contact
    form_class = ContactForm
