# Generated by Django 3.2.4 on 2022-04-21 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QVCataleg', '0007_remove_refcapa_nomcapanormalitzada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refmapawms',
            name='pCapes',
        ),
    ]
