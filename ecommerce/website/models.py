from django.db import models

class Sexual_wellness(models.Model):
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=1000, null=True)
    search_name = models.CharField(max_length=255, null=True)
    image_url = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    

class Food_bevarges(models.Model):
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=1000, null=True)
    search_name = models.CharField(max_length=255, null=True)
    image_url = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    

class Full_body_care(models.Model):
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=1000, null=True)
    search_name = models.CharField(max_length=255, null=True)
    image_url = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    

class Paper_wipes(models.Model):
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null = True)
    description = models.TextField(max_length = 1000, null = True)
    search_name = models.CharField(max_length = 255, null =True)
    image_url = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    

class Pain_relif(models.Model):
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null = True)
    description = models.TextField(max_length = 1000, null = True)
    search_name = models.CharField(max_length = 255, null =True)
    image_url = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    

class Homepathy(models.Model):
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null = True)
    description = models.TextField(max_length = 1000, null = True)
    search_name = models.CharField(max_length = 255, null =True)
    image_url = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    

class Aryuveda(models.Model):
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null = True)
    description = models.TextField(max_length = 1000, null = True)
    search_name = models.CharField(max_length = 255, null =True)
    image_url = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    

class Drinks(models.Model):
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null = True)
    description = models.TextField(max_length = 1000, null = True)
    search_name = models.CharField(max_length = 255, null =True)
    image_url = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    

class Baby_Products(models.Model):
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null = True)
    description = models.TextField(max_length = 1000, null = True)
    search_name = models.CharField(max_length = 255, null =True)
    image_url = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    

class Pet_supplies(models.Model):
    name = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null = True)
    description = models.TextField(max_length = 1000, null = True)
    search_name = models.CharField(max_length = 255, null =True)
    image_url = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
