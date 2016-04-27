# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-27 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=45)),
                ('home_number', models.IntegerField()),
                ('housing', models.CharField(blank=True, max_length=10, null=True)),
                ('flat', models.CharField(blank=True, max_length=10, null=True)),
                ('district', models.CharField(blank=True, max_length=30, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id_country', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DbHostel',
            fields=[
                ('hostel_id', models.AutoField(primary_key=True, serialize=False)),
                ('hostel_name', models.CharField(blank=True, max_length=45, null=True)),
                ('hostel_capacity', models.CharField(blank=True, max_length=45, null=True)),
                ('hostel_status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'db_hostel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DbOrder',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'db_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DbService',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=45)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('service_cost', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'db_service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DbServiceCountriesHostels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'db_service_countries_hostels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DbServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'db_service_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DbTransport',
            fields=[
                ('transport_id', models.AutoField(primary_key=True, serialize=False)),
                ('transport_name', models.CharField(max_length=45)),
                ('transport_type', models.CharField(max_length=10)),
                ('capacity', models.IntegerField()),
            ],
            options={
                'db_table': 'db_transport',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DbuClient',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=25)),
                ('client_sname', models.CharField(max_length=30)),
                ('client_fname', models.CharField(blank=True, max_length=25, null=True)),
                ('client_email', models.CharField(blank=True, max_length=45, null=True)),
                ('client_phone', models.CharField(max_length=45)),
                ('client_phone2', models.CharField(blank=True, max_length=45, null=True)),
                ('client_bdate', models.DateField()),
                ('client_job', models.CharField(blank=True, max_length=55, null=True)),
                ('client_group_head', models.BooleanField()),
            ],
            options={
                'db_table': 'dbu_client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DbuClientPassport',
            fields=[
                ('id_passport', models.AutoField(primary_key=True, serialize=False)),
                ('series', models.CharField(max_length=5)),
                ('number', models.CharField(max_length=20)),
                ('id_number', models.CharField(blank=True, max_length=20, null=True)),
                ('date_of_expiry', models.DateField()),
                ('date_of_issue', models.DateField()),
                ('authority', models.CharField(max_length=80)),
                ('nationality', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'dbu_client_passport',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dbupost',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('post', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'dbupost',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dbuser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30)),
                ('user_sname', models.CharField(max_length=30)),
                ('user_fname', models.CharField(max_length=30)),
                ('user_login', models.CharField(max_length=25)),
                ('user_password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'dbuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
    ]
