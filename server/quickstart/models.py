from django.db import models


# Create your models here.
class ExampleModel(models.Model):
    userid=models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    index = models.CharField(max_length=10000000000)

class employeeModel(models.Model):
    id=models.AutoField(primary_key=True)
    fname= models.CharField(max_length=20)
    lname= models.CharField(max_length=20)
    eid = models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    pswd = models.CharField(max_length=10000000000)
    
class appModel(models.Model):
    uid = models.CharField(max_length = 800)
    pdf = models.CharField(max_length=10000)
    email = models.CharField(max_length=200)

class tempModel(models.Model):
    uid = models.CharField(max_length= 800)
    pdf = models.CharField(max_length=10000)

class temp2Model(models.Model):
    uid = models.CharField(max_length= 800)
    pdf = models.CharField(max_length=10000)

class temp1Model(models.Model):
    uid = models.CharField(max_length= 800)
    pdf = models.CharField(max_length=10000)

class testModel(models.Model):
    uid = models.CharField(max_length= 800)
    pdf = models.CharField(max_length=10000)

class accpModel(models.Model):
    uid = models.CharField(max_length= 800)
    pdf = models.CharField(max_length=10000)

class rejectModel(models.Model):
    uid = models.CharField(max_length= 800)
    pdf = models.CharField(max_length=10000)
    reas = models.CharField(max_length= 800)

class sec_appModel(models.Model):
    uid = models.CharField(max_length= 800)
    pdf = models.CharField(max_length=10000)

class sec_accpModel(models.Model):
    uid = models.CharField(max_length= 800)
    pdf = models.CharField(max_length=10000)
    coll_d = models.CharField(max_length= 80)

class test1Model(models.Model):
    uid = models.CharField(max_length= 800)
    pdf = models.CharField(max_length=10000)


class formsModel(models.Model):
     
    title = models.CharField(max_length = 80)
    pdf = models.FileField(upload_to='pdfs/')
 
    class Meta:
        ordering = ['title']
     
    def __str__(self):
        return f"{self.title}"


