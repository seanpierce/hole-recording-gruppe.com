# Generated by Django 3.1.1 on 2024-03-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0002_release_preorder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='preorder_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
