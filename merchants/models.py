from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StoreName(models.Model):
    store_names = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.store_names}"

class MerchantName(models.Model):
    merchant_names = models.OneToOneField(User, on_delete=models.CASCADE, related_name="merchant_names", default="")
    def __str__(self):
        return f"{self.merchant_names}"

class MerchantData(models.Model):
    store_name = models.ForeignKey(StoreName, on_delete=models.CASCADE, related_name="store_name")
    merchant_name = models.ForeignKey(MerchantName, on_delete=models.CASCADE, related_name="merchant_name")

    def __str__(self):
        return f"Store: {self.store_name} = Owner: {self.merchant_name}"

class Codes(models.Model):

    code = models.CharField(max_length=8, unique=True, blank=True, null=True)
    offer = models.PositiveIntegerField(default=0)
    is_redeemed = models.BooleanField(default=False)
    minimum_value = models.PositiveIntegerField()
    date = models.DateField(max_length=300, default="")
    store_owner = models.ForeignKey(MerchantName, on_delete=models.CASCADE, related_name="store_owner")

    def __str__(self):
        return f"upto{self.offer} Code: {self.code}"

# Customer Models
class CustomerCoupon(models.Model):
    store = models.CharField(max_length=300)
    username = models.CharField(max_length=300, unique=False)
    coupon = models.CharField(max_length=300)
    is_redeemed = models.BooleanField(default=False)

    def __str__(self):
        return f"Coupon: {self.coupon} Username :{self.username}"