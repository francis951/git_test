from django.db import models

# Create your models here.
#Table with foreign key

class Carrier(models.Model):
    carrier = models.CharField(max_length=50)
    def __str__(self):
        return self.carrier
    
#table candidate
GENDER = (
    ('M', 'M'),
    ('F','F'),
)

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, null=True, choices=GENDER)
    carrier = models.ForeignKey(Carrier, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name