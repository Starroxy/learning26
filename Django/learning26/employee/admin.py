from django.contrib import admin
from .models import employee,course,college,ShopProduct
# Register your models here.

admin.site.register(employee)
admin.site.register(course)
admin.site.register(college)
admin.site.register(ShopProduct)