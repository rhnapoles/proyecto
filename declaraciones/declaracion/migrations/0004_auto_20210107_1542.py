# Generated by Django 3.0 on 2021-01-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('declaracion', '0003_auto_20201204_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='declaraciones',
            name='sello',
        ),
        migrations.AddField(
            model_name='declaraciones',
            name='extemporanea',
            field=models.BooleanField(blank=True, default=0, null=True),
        ),
    ]