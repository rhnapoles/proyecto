# Generated by Django 3.0 on 2020-11-05 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0002_sitio_personalizacion_recapthca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitio_personalizacion',
            old_name='recapthca',
            new_name='recaptcha',
        ),
    ]
