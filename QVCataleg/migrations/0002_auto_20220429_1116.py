# Generated by Django 3.2.4 on 2022-04-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QVCataleg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refmapa',
            name='codiMapa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='refmapa',
            name='nom',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='refmapa',
            name='tipus',
            field=models.CharField(max_length=20, null=True),
        ),
    ]