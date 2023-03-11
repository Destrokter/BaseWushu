from .models import Allbase
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class AllbaseForm(ModelForm):
    
    class Meta:
        model = Allbase
        fields =['name', 'birthday', 'rang', 'agegroup', 'gender', 'city_region', 'part',
                  'weightcat','trener']
        