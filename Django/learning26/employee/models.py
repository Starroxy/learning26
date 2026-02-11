from django.db import models

# Create your models here.

class employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.IntegerField()
    post=models.CharField(max_length=50)
    join_date=models.DateField(auto_now_add=True)
    
    class Meta:
        db_table="employee"
    def __str__(self):
        return self.name

class course(models.Model):
    name=models.CharField(max_length=100)
    duration=models.IntegerField()
    fee=models.IntegerField()
    class Meta:
        db_table="course"
    def __str__(self):
        return self.name

class college(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    city=models.CharField(choices=[('gandhinagar','Gandhinagar'),('ahmedabad','Ahmedabad'),('Mahesana','Mahesana')])
    Rating=models.DecimalField(max_digits=5, decimal_places=1)
    Review=models.TextField()
    
    class Meta:
        db_table="college"
    def __str__(self):
        return self.name

class ShopProduct(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(choices=[('electronics','Electronics'),('groceries','Groceries'),('books','Books')])
    price=models.IntegerField()
    quantity=models.IntegerField(default=0)
    class Meta:
        db_table="shop_product"
    def __str__(self):
        return self.name