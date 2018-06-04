from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 60)
    brand = models.CharField(max_length = 100)
    type = models.CharField(max_length = 100)
    price = models.CharField(max_length = 6, null = True)
    rating = models.CharField(max_length = 2)
    img_url = models.CharField(max_length = 2000)


    def publish(self):
        self.save()

    def __str__(self):
        return self.title
