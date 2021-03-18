from django.db import models


class MovieData(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=100, default='action')
    image = models.ImageField(upload_to='images/', default='images/none/no_img.jpg')
