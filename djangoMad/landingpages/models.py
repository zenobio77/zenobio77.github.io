from django.db import models
from PIL import Image

class Image(models.Model):

    name = models.CharField(max_length=100, default='Image')
    image = models.ImageField(default= 'default.jpg', upload_to='ladingpages_images')

    def __str__(self):
        return f'{self.name}'
