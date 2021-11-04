from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

from .models import Sezione
from .mixins import StaffMixing


class CreaSezione(StaffMixing, CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url = "/"

def visualizza_sezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    context = {"sezione": sezione}
    return render(request, "forum/singola_sezione.html", context)