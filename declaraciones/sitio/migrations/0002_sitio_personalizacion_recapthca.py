# Generated by Django 3.0 on 2020-11-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitio_personalizacion',
            name='recapthca',
            field=models.BooleanField(default=False),
        ),
    ]