from django.contrib import admin
from .models import Student,product,movie,studentprofile,review,productpirce,category,service
# Register your models here.
admin.site.register(Student)
admin.site.register(product)
admin.site.register(movie)
admin.site.register(studentprofile)
admin.site.register(review)
admin.site.register(productpirce)
admin.site.register(category)
admin.site.register(service)