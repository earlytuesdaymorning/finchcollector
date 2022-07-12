from pyexpat import model
from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User

SEX = (
    ('U', 'Unknown'),
    ('M', 'Male'),
    ('F', 'Female'),
)

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('location-detail', kwargs={'pk': self.id})

class Bird(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    adult = models.BooleanField()
    sex = models.CharField(
        max_length=1,
        choices=SEX,
        default=SEX[0][0]
    )
    locations = models.ManyToManyField(Location)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.species

    def get_absolute_url(self):
        return reverse('bird-detail', kwargs={'bird_id': self.id})
    
class Sighting(models.Model):
    datetime = models.DateTimeField('time of sighting')
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.datetime}'
    
    class Meta:
        ordering = ['-datetime']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for bird_id: {self.bird_id} @{self.url}'