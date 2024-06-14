from django.db import models

class ConcertModel(models.Model):
    name = models.CharField(max_length=100)
    singer_name = models.CharField(max_length=100)
    length = models.IntegerField()
    
    def __str__(self):
        return self.singer_name
    
class LocationModel(models.Model):
    id_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500, default="تهران-برج میلاد")
    phone = models.CharField(max_length=11, null=True)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.name

class TimeModel(models.Model):
    concert_model = models.ForeignKey("ConcertModel", on_delete=models.PROTECT)
    location_model = models.ForeignKey("LocationModel", on_delete=models.PROTECT)
    start_date_time = models.DateTimeField()
    seats = models.IntegerField()

    Start = 1
    End = 2
    Cancle = 3
    Sales = 4
    status_choices = (
        ("Start", "فروش بلیط شروع شده است"),
        ("End", "فروش بلیط تمام شده است"),
        ("Cancle", "این سانی کنسل شده است"),
        ("Salse", "درحال فروش بلیط")
    )  
    
    status = models.IntegerField(choices=status_choices)
    
    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(start_date_time,concert_model.name,location_model.name)
    