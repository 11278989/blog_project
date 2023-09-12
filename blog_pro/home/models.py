from django.db import models

# Create your models here.
class blog(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='picture')
    cate=models.CharField(max_length=50)
    desc=models.TextField()
    author=models.CharField(max_length=50)
    date=models.DateField()
        
class side_photos(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='picture')
    date=models.DateField()
        
class side_bar(models.Model):
    img=models.ImageField(upload_to='picture')
    date=models.DateField()