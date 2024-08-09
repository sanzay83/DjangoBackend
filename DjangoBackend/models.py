from django.db import models

class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=10000)
    name = models.CharField(max_length=100)  
    price = models.CharField(max_length=15)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    message = models.TextField()
    reaction = models.IntegerField()

    def __str__(self):
        return self.title