from django.db import models
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.models import User

class Allbase(models.Model):

    AGEGROUP_CHOICES = [
        ('до 8р.', 'до 8р.'),
        ('9-11р.', '9-11р.'),
        ('12-14р.', '12-14р.'),
        ('15-17р.', '15-17р.'),
        ('18+р.', '18+р.'),
        ('до 9р.', 'до 9р.'),
        ('10-11р.', '10-11р.'),
        ('12-13р.', '12-13р.'),
        ('14-15р.', '14-15р.'),
        ('16-17р.', '16-17р.'),
        ('18-40р.', '18-40р.'),
     ]
    GENDER_CHOICES = [
        ('чол', 'чол'),
        ('жін', 'жін'),
    ]
    PART_CHOICES = [
        ('таолу', 'таолу'),
        ('саньда', 'саньда'),
        ('ціньда', 'ціньда'),
        ('туйшоу', 'туйшоу'),
        ('він чун', 'він чун'),
    ]
    WEIGHTCAT_CHOICES = [
        ('до 27 кг', 'до 27 кг'),
        ('до 30 кг', 'до 30 кг'),
        ('до 33 кг', 'до 33 кг'),
        ('до 36 кг', 'до 36 кг'),
        ('до 39 кг', 'до 39 кг'),
        ('до 42 кг', 'до 42 кг'),
        ('до 45 кг', 'до 45 кг'),
        ('до 48 кг', 'до 48 кг'),
        ('48+ кг', '48+ кг'),
        ('до 52 кг', 'до 52 кг'),
        ('52+ кг', '52+ кг'),
        ('до 56 кг', 'до 56 кг'),
        ('56+ кг', '56+ кг'),
        ('до 60 кг', 'до 60 кг'),
        ('60+ кг', '60+ кг'),
        ('до 65 кг', 'до 65 кг'),
        ('65+ кг', '65+ кг'),
        ('до 70 кг', 'до 70 кг'),
        ('70+ кг', '70+ кг'),
        ('до 75 кг', 'до 75 кг'),
        ('75+ кг', '75+ кг'),
        ('до 80 кг', 'до 80 кг'),
        ('80+ кг', '80+ кг'),
        ('до 85 кг', 'до 85 кг'),
        ('до 90 кг', 'до 90 кг'),
        ('90+ кг', '90+ кг'),
    ]
    RANG_CHOICES = [
        ('І юн.', 'І юн.'),
        ('ІІ юн.', 'ІІ юн.'),
        ('ІІІ юн.', 'ІІІ юн.'),
        ('І', 'І'),
        ('ІІ', 'ІІ'),
        ('ІІІ', 'ІІІ'),
        ('КМСУ', 'КМСУ'),
        ('МСУ', 'МСУ'),
        ('МСМКУ', 'МСМКУ'),
        ('ЗМСУ', 'ЗМСУ'),
    ]
    representative = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name='Представник', blank=True, null=True)
    name = models.CharField('ПІБ', max_length=50)
    birthday = models.DateField('Дата народження')
    rang = models.CharField('Розряд',max_length=20, choices=RANG_CHOICES, default=None, blank=True)
    agegroup = models.CharField('Вікова група',max_length=20, choices=AGEGROUP_CHOICES, default=None)
    gender = models.CharField('Стать',max_length=20, choices=GENDER_CHOICES, default=None )
    city_region = models.CharField('Область, місто',max_length=50)
    part = models.CharField('Розділ',max_length=20, choices=PART_CHOICES, default=None)
    weightcat = models.CharField('Вагова категорія', max_length=20, choices=WEIGHTCAT_CHOICES, default=None, blank=True)
    trener = models.CharField('Тренер',max_length=50)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return f'/allbase/{self.id}'

    class Meta:
        verbose_name = 'База спортсменів'
        verbose_name_plural = 'База спортсменів'
        ordering = ['name']
        
