# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CompanyBranch(models.Model):
    branch_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'company_branch'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Dept(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'dept'


class EmpState(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    img = models.CharField(max_length=4000, blank=True, null=True)
    dept_id = models.CharField(max_length=50, blank=True, null=True)
    national_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_state'


class LoginEmp(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_emp'


class Offers(models.Model):
    offer_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'offers'


class OffersPi(models.Model):
    pk = models.CompositePrimaryKey('offer_id', 'pi_id')
    offer = models.ForeignKey(Offers, models.DO_NOTHING)
    pi = models.ForeignKey('PersonalInfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'offers_pi'


class PersonalInfo(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    role_cat = models.ForeignKey('Role', models.DO_NOTHING)
    emp = models.ForeignKey(EmpState, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    dept = models.ForeignKey(Dept, models.DO_NOTHING)
    branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'personal_info'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductBranch(models.Model):
    pk = models.CompositePrimaryKey('product_id', 'branch_id')
    product = models.ForeignKey(Product, models.DO_NOTHING)
    branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_branch'


class Role(models.Model):
    role_cat_id = models.AutoField(primary_key=True)
    name_of_cat = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'role'


class Storehouse(models.Model):
    storehouse_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'storehouse'


class StorehouseBranch(models.Model):
    pk = models.CompositePrimaryKey('storehouse_id', 'branch_id')
    storehouse = models.ForeignKey(Storehouse, models.DO_NOTHING)
    branch = models.ForeignKey(CompanyBranch, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'storehouse_branch'


class StorehouseProduct(models.Model):
    pk = models.CompositePrimaryKey('product_id', 'storehouse_id')
    product = models.ForeignKey(Product, models.DO_NOTHING)
    storehouse = models.ForeignKey(Storehouse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'storehouse_product'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'users'
