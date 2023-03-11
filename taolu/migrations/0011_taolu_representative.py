# Generated by Django 4.1.5 on 2023-03-09 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taolu', '0010_alter_taolu_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='taolu',
            name='representative',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Представник'),
        ),
    ]