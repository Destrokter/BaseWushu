# Generated by Django 4.1.5 on 2023-03-09 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allbase', '0003_alter_allbase_part'),
        ('tradic', '0004_alter_tradic_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradic',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='allbase.allbase', verbose_name='ПІБ'),
        ),
    ]
