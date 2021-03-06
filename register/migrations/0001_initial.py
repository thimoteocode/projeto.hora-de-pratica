# Generated by Django 3.2.5 on 2021-08-17 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='meusarquivos/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('email', models.EmailField(max_length=50)),
                ('contact', models.CharField(max_length=15)),
                ('managers', models.ManyToManyField(blank=True, related_name='company', to=settings.AUTH_USER_MODEL, verbose_name='managers')),
            ],
            options={
                'verbose_name_plural': 'Company',
            },
        ),
    ]
