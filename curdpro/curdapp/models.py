from django.db import models

class ProductData(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_cost = models.IntegerField()
    product_color = models.CharField(max_length=50)
    product_class = models.CharField(max_length=10)
    number_of_products = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    email = models.EmailField(max_length=50)