# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db.models import CASCADE, DO_NOTHING
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Activation(models.Model):
    serial1 = models.CharField(max_length=800)
    serial2 = models.CharField(max_length=800, null=True, blank=True)
    company = models.CharField(max_length=160, null=True, blank=True)
    last_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)


class Account(models.Model):
    role_admin ='المديرين'
    role_accountant = 'المحاسبين'
    role_warehouse = 'المخازن'
    role_choices = (
    (role_admin,'المديرين'),
    (role_accountant,'المحاسبين'),
    (role_warehouse,'المخازن'),
    )
    user = models.ForeignKey(User, on_delete=CASCADE)
    role = models.CharField(max_length=50,choices=role_choices)

class Company(models.Model):
    company_name = models.CharField(max_length=250)

    def __str__(self):
        return self.company_name


class Farm(models.Model):
    farm_name = models.CharField(max_length=250)

    def __str__(self):
        return self.farm_name

    def get_absolute_url(self):
        return reverse('farm_details', args=[str(self.id)])


class Job(models.Model):
    job_name = models.CharField(max_length=250)

    def __str__(self):
        return self.job_name


class Worker(models.Model):
    worker_name = models.CharField(max_length=250)
    worker_phone = models.IntegerField()
    worker_id = models.IntegerField()
    worker_address = models.CharField(max_length=500)
    worker_job = models.ForeignKey(Job, on_delete=CASCADE)
    worker_farm = models.ForeignKey(Farm, on_delete=CASCADE)
    worker_salary = models.IntegerField()
    worker_work_date = models.DateField()
    worker_image = ProcessedImageField(upload_to='media',
                                       processors=[ResizeToFill(256, 256)],
                                       format='JPEG',
                                       options={'quality': 60},
                                       blank=True)
    worker_deleted = models.BooleanField(default=False)
    worker_end_time = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.worker_name

    def get_absolute_url(self):
        return reverse('worker_details', args=[str(self.id)])


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=85)
    supplier_mob_number = models.CharField(max_length=12)
    supplier_ID_number = models.CharField(max_length=20)

    def __str__(self):
        return self.supplier_name

    def get_absolute_url(self):
        return reverse('supplier_details', args=[str(self.id)])


class Client(models.Model):
    client_name = models.CharField(max_length=85)
    client_mobile_number = models.CharField(max_length=12)
    client_ID_number = models.CharField(max_length=20)
    client_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.client_name

    def get_absolute_url(self):
        return reverse('client_details', args=[str(self.id)])


class Product(models.Model):
    product_name = models.CharField(max_length=160)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product_details', args=[str(self.id)])


class Warehouse(models.Model):
    item_name = models.ForeignKey(Product, on_delete=CASCADE)
    item_quantity = models.IntegerField()
    farm = models.ForeignKey(Farm, on_delete=CASCADE)

    def __str__(self):
        return self.item_name.product_name


class Balance(models.Model):
    farm = models.ForeignKey(Farm, on_delete=CASCADE)
    balance = models.IntegerField()


class Type(models.Model):
    type_name = models.CharField(max_length=80)

    def __str__(self):
        return self.type_name


class Category(models.Model):
    category_name = models.CharField(max_length=80)
    type = models.ForeignKey(Type, on_delete=CASCADE)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('add_tawseef')


class Daily(models.Model):
    date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=80)
    maden = models.IntegerField(default=0)
    maden_from_type = models.ForeignKey(Type, on_delete=CASCADE, blank=True, null=True)
    maden_from_cat = models.ForeignKey(Category, on_delete=CASCADE, blank=True, null=True)
    da2en = models.IntegerField(default=0)
    da2en_from_type = models.ForeignKey(Type, on_delete=CASCADE, related_name='da2en_from_type', blank=True, null=True)
    da2en_from_cat = models.ForeignKey(Category, on_delete=CASCADE, related_name='da2en_from_cat', blank=True,
                                       null=True)
    paid = models.IntegerField()
    unpaid = models.IntegerField()
    farm = models.ForeignKey(Farm, on_delete=CASCADE)
    is_invoice = models.BooleanField(default=False)


class BuyInvoice(models.Model):
    date = models.DateField(auto_now=True)
    supplier = models.ForeignKey(Supplier, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=CASCADE)
    farm = models.ForeignKey(Farm, on_delete=CASCADE)


class SellInvoice(models.Model):
    date = models.DateField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    unpaid = models.IntegerField()
    paid = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=CASCADE)
    farm = models.ForeignKey(Farm, on_delete=CASCADE)


class Talabat(models.Model):
    date = models.DateField(auto_now=True)
    farm = models.ForeignKey(Farm, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField()
    OK = models.BooleanField(default=False)


class Mezan(models.Model):
    name = models.ForeignKey(Category, on_delete=CASCADE)
    da2en = models.IntegerField(default=0)
    maden = models.IntegerField(default=0)
