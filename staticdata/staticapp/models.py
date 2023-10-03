from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics')
    discription = models.TextField()
    def __str__(self) :
        return self.name
    
class Mentors(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='mentors')
    discrption = models.TextField()

    def __str__(self):
        return self.name