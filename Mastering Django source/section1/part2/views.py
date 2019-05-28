from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Author, Contact
from .forms import ContactForm


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']


class ContactUpdate(UpdateView):
    model = Contact
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        kwargs = super(ContactUpdate, self).get_context_data(**kwargs)
        kwargs.update({'form2':AnotherForm()})

        return kwargs
