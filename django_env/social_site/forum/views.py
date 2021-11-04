from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Sezione


class CreaSezione(CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url = "/"
