from django.db import models

class ConsertModel(models.Model):
    name = models.CharField(max_length=100)
    singer_name = models.CharField(max_length=100)
    length = models.IntegerField()
    
    def __str__(self):
        return self.singer_name
    
class locationModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=11)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
    