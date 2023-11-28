from django.db import models

# Create your models here.
class offreg_tbl(models.Model):
    unm = models.CharField(max_length=50)
    em = models.EmailField()
    oid = models.CharField(max_length=50)
    psw = models.CharField(max_length=16)
class cmnt_tbl(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
class news_tbl(models.Model):
    title = models.CharField(max_length=200)
    athr = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    img = models.FileField(upload_to="upload")
