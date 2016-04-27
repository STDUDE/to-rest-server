# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=45)
    home_number = models.IntegerField()
    housing = models.CharField(max_length=10, blank=True, null=True)
    flat = models.CharField(max_length=10, blank=True, null=True)
    district = models.CharField(max_length=30, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    city = models.ForeignKey('City', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'address'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=45)
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    id_country = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'

    def __unicode__(self):
        return "/%s/" % self.country

    def get_name(self):
        return "/%s/" % self.country

    def is_true(self):
        if self.id_country > 400:
            return True
        else:
            return False


class DbHostel(models.Model):
    hostel_id = models.AutoField(primary_key=True)
    hostel_name = models.CharField(max_length=45, blank=True, null=True)
    hostel_address = models.ForeignKey(Address, models.DO_NOTHING, db_column='hostel_address', blank=True, null=True)
    hostel_capacity = models.CharField(max_length=45, blank=True, null=True)
    hostel_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_hostel'


class DbOrder(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_service = models.ForeignKey('DbService', models.DO_NOTHING, db_column='id_service', blank=True, null=True)
    id_head = models.ForeignKey('DbuClient', models.DO_NOTHING, db_column='id_head', blank=True, null=True)
    order_date = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_order'


class DbService(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=45)
    service_type = models.ForeignKey('DbServiceType', models.DO_NOTHING)
    begin_date = models.DateField()
    end_date = models.DateField()
    begin_transport = models.ForeignKey('DbTransport', models.DO_NOTHING, db_column='begin_transport', related_name='begin_transport')
    end_transport = models.ForeignKey('DbTransport', models.DO_NOTHING, db_column='end_transport')
    service_cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_service'


class DbServiceCountriesHostels(models.Model):
    service = models.ForeignKey(DbService, models.DO_NOTHING)
    country = models.ForeignKey(Country, models.DO_NOTHING)
    hostel = models.ForeignKey(DbHostel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'db_service_countries_hostels'
        unique_together = (('service', 'country', 'hostel'),)


class DbServiceType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'db_service_type'


class DbTransport(models.Model):
    transport_id = models.AutoField(primary_key=True)
    transport_name = models.CharField(max_length=45)
    transport_type = models.CharField(max_length=10)
    capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'db_transport'


class DbuClient(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=25)
    client_sname = models.CharField(max_length=30)
    client_fname = models.CharField(max_length=25, blank=True, null=True)
    client_email = models.CharField(max_length=45, blank=True, null=True)
    client_phone = models.CharField(max_length=45)
    client_phone2 = models.CharField(max_length=45, blank=True, null=True)
    client_bdate = models.DateField()
    client_job = models.CharField(max_length=55, blank=True, null=True)
    client_passport = models.ForeignKey('DbuClientPassport', models.DO_NOTHING, db_column='client_passport')
    client_address = models.ForeignKey(Address, models.DO_NOTHING, db_column='client_address')
    client_group_head = models.BooleanField()
    client_group_head_0 = models.ForeignKey('self', models.DO_NOTHING, db_column='client_group_head_id', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'dbu_client'


class DbuClientPassport(models.Model):
    id_passport = models.AutoField(primary_key=True)
    series = models.CharField(max_length=5)
    number = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_expiry = models.DateField()
    date_of_issue = models.DateField()
    authority = models.CharField(max_length=80)
    nationality = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'dbu_client_passport'


class Dbupost(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'dbupost'


class Dbuser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_sname = models.CharField(max_length=30)
    user_fname = models.CharField(max_length=30)
    user_login = models.CharField(max_length=25)
    user_password = models.CharField(max_length=20)
    user_post = models.ForeignKey(Dbupost, models.DO_NOTHING, db_column='user_post')

    class Meta:
        managed = False
        db_table = 'dbuser'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=45)
    country = models.ForeignKey(Country, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region'
