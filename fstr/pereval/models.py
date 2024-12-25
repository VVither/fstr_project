from django.db import models

class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    otc = models.CharField(max_length=255, blank=True, null=True)

class pereval_added(models.Model):
    beautyTitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True, null=True)
    connect = models.CharField(max_length=255, blank=True, null=True)
    add_time = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords_id = models.ForeignKey(Coords, on_delete=models.CASCADE)
    winter_level = models.CharField(max_length=4)
    summer_level = models.CharField(max_length=4)
    autumn_level = models.CharField(max_length=4)
    spring_level = models.CharField(max_length=4)
    status = models.CharField(max_length=50, default="new")

class images(models.Model):
    image_url = models.URLField()
    image_title = models.CharField(max_length=255, blank=True, null=True)

class PerevalImage(models.Model):
    pereval = models.ForeignKey(pereval_added, on_delete=models.CASCADE)
    images = models.ForeignKey(images, on_delete=models.CASCADE)