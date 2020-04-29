from django.db import models
from enum import Enum
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture_owner = models.ImageField(
        upload_to='uploads', null=True, blank=True)

    def __str__(self):
        return self.user


class StateChoices(Enum):
    QUEUING = "Queuing"
    DOING = "Doing"
    DONE = "Done"


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=10, choices=[(
        tag, tag.value) for tag in StateChoices], default=StateChoices.QUEUING, null=True, blank=True)
    total_price = models.FloatField(max_length=10, null=True, blank=True)
    date_time = models.DateTimeField(blank=True, auto_now_add=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    open_time = models.TimeField(blank=True, null=True)
    close_time = models.TimeField(blank=True, null=True)
    picture_restaurant = models.ImageField(
        upload_to='uploads', null=True, blank=True)
    restaurant_name = models.CharField(max_length=50, null=True, blank=True)
    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, null=True, blank=True)
    types = models.ForeignKey(
        Type, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.restaurant_name


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=50, null=True, blank=True)
    picture = models.ImageField(upload_to='uploads', null=True, blank=True)
    price = models.FloatField(max_length=10, null=True, blank=True)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True, blank=True)


class Order_List(models.Model):
    list_no = models.AutoField(primary_key=True)
    unit = models.IntegerField(null=True, blank=True)
    price = models.FloatField(max_length=50, null=True, blank=True)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, null=True, blank=True)
