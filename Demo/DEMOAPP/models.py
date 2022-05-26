from django.db import models
from django.db.models import CharField


class Post(models.Model):
    username = models.CharField(max_length=100, unique=True)
    passw =models.CharField(max_length=100)

    class Meta:
        db_table="login2"

class Signup(models.Model):
        objects = models.Manager()
        an = models.CharField(max_length=16, unique=True)
        mn = models.CharField(max_length=11)
        cid= models.CharField(max_length=9)
        cpass = models.CharField(max_length=20)
        class Meta:
            db_table = "signup3"

class log(models.Model):
    cid=models.CharField(max_length=9)
    passw=models.CharField(max_length=20)

    class Meta:
        db_table = "login3"

class Signup1(models.Model):
    objects = models.Manager()
    an = models.CharField(max_length=16, unique=True)
    mn = models.CharField(max_length=11)
    cid = models.CharField(max_length=9,primary_key = True)
    cpass = models.CharField(max_length=20)

    class Meta:
        db_table = "signup4"

class personalbanking(models.Model):
    cid = models.CharField(max_length=9)
    AN = models.CharField(max_length=16)
    CN = models.CharField(max_length=11)
    Amt = models.CharField(max_length=10)
    email = models.CharField(max_length=20)

    class Meta:
        db_table = "personal"

class personalbanking2(models.Model):
    AN = models.CharField(max_length=16)
    CN = models.CharField(max_length=11)
    Amt = models.CharField(max_length=10)
    email = models.CharField(max_length=20)

    class Meta:
        db_table = "personal2"

class personalbanking3(models.Model):
    objects = models.Manager()
    cid = models.CharField(max_length=9)
    AN = models.CharField(max_length=16)
    CN = models.CharField(max_length=11)
    Amt = models.CharField(max_length=10)
    email = models.CharField(max_length=20)

    class Meta:
        db_table = "personal3"

class transaction(models.Model):
    cid = models.CharField(max_length=9)

class transaction1(models.Model):
    cid= models.CharField(max_length=9)

    class Meta:
        db_table = "trans"

class electrical(models.Model):
    cname = models.CharField(max_length=17)
    cid = models.CharField(max_length=9)
    Service = models.CharField(max_length = 20)
    bill=models.CharField(max_length = 20)

    class Meta:
        db_table = "electrical"

class mobile(models.Model):
    mn = models.CharField(max_length=11)
    cid = models.CharField(max_length=9)
    sim = models.CharField(max_length=20)
    bill = models.CharField(max_length=20)

    class Meta:
        db_table = "mobile"

class loanapp(models.Model):
    cid=models.CharField(max_length=9)
    amt=models.CharField(max_length=20)
    ir = models.CharField(max_length=20)
    months=models.CharField(max_length=20)

    class Meta:
        db_table = "loan"

class mobile2(models.Model):
    cid = models.CharField(max_length=9)
    sim = models.CharField(max_length=9)
    mn = models.CharField(max_length=11)
    bill = models.CharField(max_length=20)

    class Meta:
        db_table = "mobile2"

class insurance(models.Model):
    cid = models.CharField(max_length=9)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mn = models.CharField(max_length=11)
    address = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    loan = models.CharField(max_length=40)

    class Meta:
        db_table="insurance"

class insurance2(models.Model):
    cid = models.CharField(max_length=9)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mn = models.CharField(max_length=11)
    address = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    loan = models.CharField(max_length=40)

    class Meta:
        db_table="insurance1"

