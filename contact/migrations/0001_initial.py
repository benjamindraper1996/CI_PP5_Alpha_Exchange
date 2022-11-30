# Generated by Django 3.2 on 2022-11-29 00:58

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(max_length=80)),
                ('town_or_city', models.CharField(max_length=40)),
                ('county', models.CharField(max_length=80)),
                ('postcode', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('message', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]