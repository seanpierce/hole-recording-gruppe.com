# Generated by Django 3.1.1 on 2024-04-01 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0004_auto_20240401_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='link_to_purchase',
            field=models.URLField(blank=True, null=True),
        ),
    ]
