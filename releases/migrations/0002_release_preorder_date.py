# Generated by Django 3.1.1 on 2024-03-27 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='preorder_date',
            field=models.DateField(null=True),
        ),
    ]
