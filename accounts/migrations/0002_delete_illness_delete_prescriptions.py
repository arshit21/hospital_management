# Generated by Django 4.1.7 on 2023-06-10 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='illness',
        ),
        migrations.DeleteModel(
            name='prescriptions',
        ),
    ]
