from django.db import models

class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=10000)
    name = models.CharField(max_length=100)  
    price = models.CharField(max_length=15)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)  
    passw = models.CharField(max_length=15)

    
