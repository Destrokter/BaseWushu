from .models import Tradic
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class TradicForm(ModelForm):

    class Meta:
        model = Tradic
        fields =['measure','name', 'birthday', 'rang', 'agegroup', 'gender', 'city_region', 'catquan',
                 'catqise',  'duilian', 'trener', 'note']