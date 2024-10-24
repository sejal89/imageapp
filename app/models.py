from django.db import models

# Create your models here.
class Album(models.Model):
    image_name = models.CharField(max_length=50)
    album_Img = models.ImageField(upload_to='images/')
    
    def __str__(self):
         return f"{self.image_name}"