# admin : khatib and 123
from django.db import models

# Create your models here.

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    decs = models.CharField(max_length=300)
    image = models.ImageField(upload_to="shop/images", default="")
    publish_date = models.DateField()

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    # msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=12, default="")
    address = models.CharField(max_length=150, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=150)
    alternate_address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

def __str__(self):
    return self.update_desc[0:10] + "..."


    


   
