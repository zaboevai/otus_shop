# Generated by Django 2.2.5 on 2019-09-10 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook_shop', '0006_auto_20190910_0824'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Good',
            new_name='Goods',
        ),
    ]