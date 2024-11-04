from app.models import Contact
from django import forms

class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name','last_name','email','content'
        ]