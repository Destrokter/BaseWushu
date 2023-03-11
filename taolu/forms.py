from .models import Taolu
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class TaoluForm(ModelForm):
    
    class Meta:
        model = Taolu
        fields =['measure','name', 'birthday', 'rang', 'agegroup', 'gender', 'city_region', 'catquan',
                  'catduanqise', 'catchanqise', 'duilian', 'trener', 'note']
       