# Generated by Django 5.0.6 on 2024-06-28 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('object_detection', '0002_alter_detectedobject_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagefeed',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]
