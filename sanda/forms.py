from .models import Sanda
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class SandaForm(ModelForm):
    
    class Meta:
        model = Sanda
        fields =['measure','name', 'birthday', 'rang', 'agegroup', 'gender', 'city_region', 'part',
                  'weightcat','trener', 'note']
        