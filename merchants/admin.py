from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StoreName)
admin.site.register(MerchantName)
admin.site.register(MerchantData)
admin.site.register(Codes)
admin.site.register(CustomerCoupon)