from django.db import models


class Lot(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='lot/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
