from django.contrib import admin
from .models import Taolu

class TaoluAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'rang', 'agegroup', 'gender', 'city_region', 'catquan',
                     'catduanqise', 'catchanqise', 'duilian', 'trener', 'note')
    list_display_links = ('name', 'trener')
    search_fields = ('name', 'trener')
    list_filter = ('measure','agegroup', 'gender', 'city_region', 'catquan',
            'catduanqise', 'catchanqise', 'duilian', 'trener', 'note')
    save_on_top = True


admin.site.register(Taolu, TaoluAdmin)

