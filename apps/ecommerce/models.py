# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
from django.core.files.images import ImageFile
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) == 0:
            errors['first_name'] = "Please enter a first name"
        elif len(postData['first_name']) < 3:
            errors['first_name'] = "First name should be more than 2 characters"
        elif any([letter.isdigit() for letter in postData['first_name']]):
            errors['first_name'] = "First name must only contains letters"

        if len(postData['last_name']) == 0:
            errors['last_name'] = "Please enter a last name"
        elif len(postData['last_name']) < 3:
            errors['last_name'] = "Last name should be more than 2 characters"
        elif any([letter.isdigit() for letter in postData['last_name']]):
            errors['last_name'] = "Last name must only contains letters"

        if len(postData['email']) == 0:
            errors['email'] = "Enter a valid email"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email in email format"
        else:
            try:
                User.objects.get(email=postData['email'])
                errors['email'] = "Email is already registered, please enter another"
            except ObjectDoesNotExist:
                pass

        if len(postData['password']) == 0:
            errors['password'] = "Please enter a password"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be longer than 8 characters"
        if postData['password'] != postData['cpass']:
            errors['password'] = "Confirmation password does not match the password"
        return errors;

    def basic_login_validator(self, postData):
        errors = {}
        if len(postData['email']) == 0:
            errors['email'] = "Please enter an email"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email in email format"
        else:
            try:
                user = User.objects.get(email=postData['email'])
                if bcrypt.checkpw(postData['password'].encode(), user.password.encode()) != True:
                    errors['password'] = "Email and password doesn't match"
            except ObjectDoesNotExist:
                errors['password'] = "Email is not registered, please register first"
        if len(postData['password']) == 0:
            errors['password'] = "Please enter a password"
        return errors;

    def buy_validator(self, postData):
        errors = {}
        if len(postData['first_name']) == 0:
            errors['first_name'] = "Please enter a first name"
        elif len(postData['first_name']) < 3:
            errors['first_name'] = "First name should be more than 2 characters"

        if len(postData['last_name']) == 0:
            errors['last_name'] = "Please enter a last name"
        elif len(postData['last_name']) < 3:
            errors['last_name'] = "Last name should be more than 2 characters"

        if len(postData['address']) == 0:
            errors['address'] = "Please enter a valid address"

        if len(postData['city']) == 0:
            errors['city'] = "Please enter a valid city"

        if len(postData['state']) == 0:
            errors['state'] = "Please enter a state"

        if len(postData['zipcode']) == 0:
            errors['zipcode'] = "Please enter a valid zipcode."
        elif any([digit.isalpha() for digit in postData['zipcode']]):
            errors['zipcode'] = "Zipcode must be numbers only."

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    admin = models.BooleanField(default=0)

    objects=UserManager()


class Shipping(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    objects=UserManager()

class Billing(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    objects=UserManager()

class Account(models.Model):
    account = models.OneToOneField(User, primary_key=True)
    biling_add = models.ManyToManyField(Billing, related_name="billing")
    shipping_add = models.ManyToManyField(Shipping, related_name="shipping")

class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to = "img/", default = "img/None")
    desc = models.TextField()
    quantity = models.IntegerField(default=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    OFFICE = "OFFICE SUPPLIES"
    BURRITO = "BURRITO"
    DOJOBELT = "DOJO BELT"
    LAWNCHAIR = "LAWN CHAIR"
    CATEGORY_CHOICES = (
        (OFFICE, "Office Supplies"),
        (BURRITO, "Burrito"),
        (DOJOBELT, "Dojo Belt"),
        (LAWNCHAIR, "Lawn Chair"),
    )
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default="OFFICE")

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    accounts = models.ForeignKey(Account, related_name = "account_cart")
    items = models.ManyToManyField(Item, related_name="item")
    PROGRESS = "IN PROGRESS"
    SHIP = "SHIPPED"
    CANCEL = "CANCELLED"

    STATUS_CHOICES = (
        (PROGRESS, "In Progress"),
        (SHIP, "Shipped"),
        (CANCEL, "Cancelled"),
    )
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default="PROGRESS")
