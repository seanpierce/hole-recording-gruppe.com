# Generated by Django 5.0.3 on 2024-03-22 22:58

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='info',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
    ]