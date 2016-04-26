from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'country'


class Region(models.Model):
    region = models.CharField(max_length=45)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'region'


class City(models.Model):
    city = models.CharField(max_length=45)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'city'


class Address(models.Model):
    street = models.CharField(max_length=45)
    home_number = models.IntegerField()
    housing = models.CharField(blank=True, max_length=10) # почитать по blank
    flat = models.CharField(blank=True, max_length=10)
    district = models.CharField(blank=True, max_length=30)
    postal_code = models.CharField(blank=True, max_length=10)
    phone = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'address'

class Hotel(models.Model):
    name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    capacity = models.CharField(max_length=45)
    status = models.IntegerField()
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'db_hostel'

class ServiseType(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'db_service_type'

class Transport(models.Model):
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=10)
    capacity = models.IntegerField(default=0)
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'db_transport'

class Service(models.Model):
    name = models.CharField(max_length=45)
    type = models.ForeignKey(ServiseType) #правильное удаление сюда добавить
    begin_date = models.DateField()
    end_date = models.DateField()
    begin_transport = models.ForeignKey(Transport)
    end_transport = models.ForeignKey(Transport)
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'db_service'

class Passport(models.Model):
    series = models.CharField(max_length=5)
    number = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    date_of_expiry = models.DateField()
    date_of_issue = models.DateField()
    authority = models.CharField(max_length=80, blank=True)
    nationaloty = models.CharField(max_length=45)
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'db_client_passport'

class Client(models.Model):
    name = models.CharField(max_length=25)
    sname = models.CharField(max_length=30)
    fname = models.CharField(max_length=25)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    phone2 = models.CharField(max_length=45, null=True)
    bdate = models.DateField()
    job = models.CharField(max_length=55, null=True)
    passport = models.ForeignKey(Passport, on_delete=models.CASCADE)
    address = models.ForeignKey(Address)
    #head ссылка на самого себя
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'dbu_client'

class Order(models.Model):
    service = models.ForeignKey(Service)
    head = models.ForeignKey(Client)
    order_date = models.DateField()
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'db_order'

class ServicesCountriesHotels(models.Model):
    service = models.ForeignKey(Service)
    country = models.ForeignKey(Country)
    hotel = models.ForeignKey(Hotel)
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'db_service_countries_hostels'

class UserPost(models.Model):
    post = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'dbupost'

class User(models.Model):
    name = models.CharField(max_length=30)
    sname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    post = models.ForeignKey(UserPost)
    order = models.ForeignKey(Order) #доработать чуть-чуть
    class Meta:
        managed = False
        db_tablespace = 'torest_db'
        db_table = 'dbuser'