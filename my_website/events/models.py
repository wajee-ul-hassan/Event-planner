from django.db import models

# Create your models here.
class Venue(models.Model):
    name=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    zip_code=models.CharField(max_length=120)
    phone=models.CharField(max_length=12)
    web=models.URLField()
    email_address=models.EmailField()

    
    def __str__(self):
        return self.name

    
class Member(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    email_address=models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
       
class Event(models.Model):
    name=models.CharField(max_length=120)
    event_date=models.DateTimeField()
    venue=models.ForeignKey(Venue,on_delete=models.CASCADE,blank=True,null=True)
    manager=models.CharField(max_length=120)
    description=models.TextField()
    members=models.ManyToManyField(Member,blank=True)
 
    def __str__(self):
        return self.name
 