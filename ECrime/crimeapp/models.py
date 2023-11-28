from django.db import models

# Create your models here.
class reg_tbl(models.Model):
    fn = models.CharField(max_length=50)
    lm = models.CharField(max_length=50)
    mb = models.IntegerField()
    em = models.EmailField()
    ps = models.CharField(max_length=16)
    

class crime_tbl(models.Model):
    name = models.CharField(max_length=50)
    pname = models.CharField(max_length=50)
    age = models.IntegerField()
    add = models.CharField(max_length=200)
    gen = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    regdt = models.CharField(max_length=50)
    comp = models.CharField(max_length=200)
    sec = models.CharField(max_length=50)
    comptyp = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    # sts = models.BooleanField(default=False)
    


class miss_tbl(models.Model):
    fname = models.CharField(max_length=50)
    # alias = models.CharField(max_length=50)
    nmb = models.IntegerField()
    eml = models.EmailField()
    relnm = models.CharField(max_length=50)
    rlty = models.CharField(max_length=50)
    # add = models.CharField(max_length=150)
    gd = models.CharField(max_length=50)
    age =models.IntegerField()
    yob = models.CharField(max_length=50)
    bb = models.CharField(max_length=50)
    bc = models.CharField(max_length=50)
    wt = models.IntegerField()
    ht = models.IntegerField()
    img = models.FileField(upload_to="missing")
    m_status = models.BooleanField(default=False)
    # sts_m = models.BooleanField(default=False)

class report_tbl(models.Model):
    loc = models.CharField(max_length=50)
    q2 = models.CharField(max_length=50)
    bt = models.CharField(max_length=50)
    bb = models.CharField(max_length=50)
    q5 = models.CharField(max_length=50)
    des = models.CharField(max_length=150)
    q7 = models.FileField(upload_to="image")
    q8 =models.CharField(max_length=150)
    r_status = models.BooleanField(default=False)
    # sts_r = models.BooleanField(default=False)



# class Complaint(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     status = models.CharField(max_length=20, default='Pending')

# class News(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='news_images')