# Generated by Django 3.2.4 on 2022-04-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QVCataleg', '0004_refmapawms_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='refmapawms',
            name='mapa_actual',
            field=models.BooleanField(default=False),
        ),
    ]