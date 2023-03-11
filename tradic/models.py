from django.db import models
from datetime import datetime
from allbase.models import Allbase
from django.contrib.auth.models import User

class Tradic(models.Model):

    AGEGROUP_CHOICES = [
        ('до 8р.', 'до 8р.'),
        ('9-11р.', '9-11р.'),
        ('12-14р.', '12-14р.'),
        ('15-17р.', '15-17р.'),
        ('18+р.', '18+р.'),
    ]
    GENDER_CHOICES = [
        ('чол', 'чол'),
        ('жін', 'жін'),
    ]
    CATQUAN_CHOICES = [
        ('ней цзя цюань', 'ней цзя цюань'),
        ('вай цзя цюань', 'вай цзя цюань'),
        ('нань цюань', 'нань цюань'),
        ('тай цзі цюань', 'тай цзі цюань'),
        ('сян сін цюань', 'сян сін цюань'),
        ('шао лінь цюань', 'шао лінь цюань'),
        ('ді тан цюань', 'ді тан цюань'),
        ('він чун цюань', 'він чун цюань'),
    ]
    CATQISE_CHOICES = [
        ('довга зброя', 'довга зброя'),
        ('коротка зброя', 'коротка зброя'),
        ('парна зброя', 'парна зброя'),
        ('гнучка зброя', 'гнучка зброя'),
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
    measure = models.CharField('Назва заходу', max_length=100, default=None)
    name = models.ForeignKey(Allbase, on_delete=models.PROTECT, verbose_name='ПІБ')
    birthday = models.DateField('Дата народження')
    rang = models.CharField('Розряд',max_length=20, choices=RANG_CHOICES, default=None, blank=True)
    agegroup = models.CharField('Вікова група',max_length=20, choices=AGEGROUP_CHOICES, default=None)
    gender = models.CharField('Стать',max_length=20, choices=GENDER_CHOICES, default=None )
    city_region = models.CharField('Область, місто',max_length=50)
    catquan = models.CharField('Категорія кулаків',max_length=20, choices=CATQUAN_CHOICES, default=None, blank=True)
    catqise = models.CharField('Категорія зброї', max_length=20, choices=CATQISE_CHOICES, default=None, blank=True)
    duilian = models.CharField('Дуйлянь',max_length=50, blank=True)
    trener = models.CharField('Тренер',max_length=50)
    note = models.CharField('Примітки', max_length=100, default=None, blank=True)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return f'/tradic/{self.id}'

    class Meta:
        verbose_name = 'Традиційні комплекси'
        verbose_name_plural = 'Традиційні комплекси'
