from django.contrib import admin
from .models import Allbase

class AllbaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'rang', 'agegroup', 'gender', 'city_region', 'part',
            'weightcat', 'trener')
    list_display_links = ('name', 'trener')
    search_fields = ('name', 'trener')
    list_filter = ('agegroup', 'gender', 'city_region', 'part',
            'weightcat', 'trener')
    save_on_top = True

admin.site.register(Allbase, AllbaseAdmin)