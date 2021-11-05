from django import forms

from .models import Discussione


class DiscussioneModelForm(forms.ModelForm):
    contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Di cosa vuoi parlarci?"}),
                                max_length=4000,
                                label="Primo messaggio")
    
    class Meta:
        model = Discussione
        fields = ["titolo", "contenuto"]
        widget = {"titolo": forms.TextInput(attrs={"placeholder": "Titolo della Discussione"})}