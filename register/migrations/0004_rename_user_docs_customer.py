# Generated by Django 3.2.5 on 2021-08-26 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_company_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docs',
            old_name='user',
            new_name='customer',
        ),
    ]